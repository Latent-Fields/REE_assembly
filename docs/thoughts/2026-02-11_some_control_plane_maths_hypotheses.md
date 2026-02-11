Status: processed

Processed in:
- `docs/architecture/mode_manager.md` (MECH-047)
- `docs/architecture/control_plane.md` (MECH-048)

---

Control plane maths for REE

Below is a minimal-but-expressive mathematical “control plane” that supports:
	•	Discrete-ish modes with soft priors (not a hard switch)
	•	A Pre-Commitment Mode Manager (PCM) that commits with hysteresis
	•	An Amygdala Analogue (AA) that updates mode priors fast
	•	μ (mu) / κ (kappa) opioid analogues as opponent entropy / stability modulators
	•	Mode-dependent precision, learning rate, and horizon length


⸻

1) Objects

Let there be K control-plane modes m \in \{1,\dots,K\} (Explore, Defend, Bond, Exploit, Rest, …).

At time t:
	•	z_t: fused latent state (from E1/E2)
	•	u_t: interoceptive / energy state summary
	•	s_t: social context summary
	•	\varepsilon_t: novelty / uncertainty / prediction error features
	•	b_t: harm / threat features (not necessarily raw nociception; includes learned threat)

Control plane maintains:
	•	Mode belief (soft): q_t(m)\in\Delta^K (a categorical distribution)
	•	Committed mode (hard): c_t \in \{1,\dots,K\} (what the system is currently running)
	•	Commitment inertia: I_t \ge 0 (how “sticky” the current mode is)

⸻

2) Amygdala Analogue (AA): fast salience → mode priors

AA produces logits \ell_t(m) from fast features:

\ell_t(m) = w_m^\top \phi(z_t,u_t,s_t,\varepsilon_t,b_t) + \beta_m

Convert to a proposal distribution (soft priors):

\tilde q_t(m) = \mathrm{softmax}(\ell_t(m))

Interpretation: AA answers “what kind of situation is this?” and outputs a distribution over regimes.

⸻

3) Opioid overlays as stability/entropy control

Define two global modulators:
	•	\mu_t \ge 0: μ-analogue (stabilise / settle / bind)
	•	\kappa_t \ge 0: κ-analogue (destabilise / re-evaluate / aversive bias)

A clean control-plane role for these is to modulate temperature (entropy) of mode beliefs and switching cost.

Entropy temperature:

\tau_t = \tau_0 \, \exp(\alpha_\kappa \kappa_t - \alpha_\mu \mu_t)

Then AA’s proposal is “sharpened” or “flattened”:

q^{AA}_t(m) = \mathrm{softmax}\!\left(\frac{\ell_t(m)}{\tau_t}\right)
	•	Higher \mu_t → lower \tau_t → more peaked q (settling / commitment)
	•	Higher \kappa_t → higher \tau_t → flatter q (uncertainty / switching pressure)

That’s the “opioids as policy-entropy modulators” idea in one line.

Switching cost / inertia update:

Let switching inertia increase with \mu and decrease with \kappa:

I_{t+1} = \lambda I_t + \eta_\mu \mu_t - \eta_\kappa \kappa_t
\quad\text{clipped to }[0,I_{\max}]

This is the second, complementary role: not just “belief entropy,” but “actual stickiness.”

⸻

4) PCM: commitment with hysteresis

PCM takes AA’s current recommendation q^{AA}_t and decides whether to stay in c_t or switch.

Define a switch score for candidate mode m:

S_t(m) = \log q^{AA}_t(m) - \log q^{AA}_t(c_t) - \underbrace{I_t}_{\text{inertia}} - \underbrace{\Gamma_t(m,c_t)}_{\text{transition cost}}

Where \Gamma_t(m,c) is optional structure: some transitions are “harder” (e.g., Rest → Defend might be fast; Bond → Defend might be expensive or vice versa depending on design).

PCM rule (simple):

c_{t+1} =
\begin{cases}
\arg\max_m S_t(m) & \text{if } \max_m S_t(m) > \theta_t \\
c_t & \text{otherwise}
\end{cases}

Threshold \theta_t can itself be modulated (stress reduces threshold; μ raises it):

\theta_t = \theta_0 + \rho_\mu \mu_t - \rho_\kappa \kappa_t

So:
	•	High \mu_t: harder to switch (commitment stabilised)
	•	High \kappa_t: easier to switch (re-evaluation pressure)

⸻

5) Mode-dependent precision, learning rate, and horizon

Once committed mode c_t is set, it configures downstream parameters.

Let each mode have a parameter bundle:
	•	Precision gain multiplier g_\pi(m)
	•	Learning-rate multiplier g_\eta(m)
	•	Horizon multiplier g_T(m)

Then:

Policy precision (for E3 trajectory selection):
\Pi_t = \Pi_0 \cdot g_\pi(c_t)\cdot f_\Pi(\text{arousal}_t)

Learning rate:
\eta_t = \eta_0 \cdot g_\eta(c_t)\cdot f_\eta(\varepsilon_t,b_t)

Planning horizon:
T_t = T_0 \cdot g_T(c_t)\cdot f_T(u_t,b_t)

Typical shape (illustrative):
	•	Explore: high T, moderate \Pi, higher \eta
	•	Defend: low T, high \Pi (tight action), higher \eta for threat cues
	•	Bond: moderate-high T, social-feature precision upweighted, learning emphasises social memory
	•	Rest: low \Pi, low \eta, “offline consolidation” flags

⸻

6) How this plugs into E3 trajectory search

Let E3 generate candidate trajectories \tau\in\mathcal{T} (not to confuse with temperature). Score them with a mode-conditioned objective:

J(\tau \mid c_t) =
\mathbb{E}\left[\sum_{k=0}^{T_t}
\gamma^k
\Big(
- \lambda_H \hat H_{t+k}
+ \lambda_C \hat C_{t+k}
\Big)\right]

Where:
	•	\hat H is predicted harm / constraint violation
	•	\hat C is predicted coherence / goal progress / social alignment (whatever REE uses as “good trajectory”)
	•	\lambda_H,\lambda_C are mode-shaped (Defend increases \lambda_H; Explore increases tolerance)

Then E3 selects stochastically with precision \Pi_t:

P(\tau) \propto \exp(\Pi_t \, J(\tau\mid c_t))

This is where “mode” becomes actual behaviour.

⸻

7) Minimal μ/κ dynamics you can implement without overclaiming

If you want μ/κ analogues to be computed (not just hand-set), you can tie them to very conservative signals:
	•	\mu_t increases when threat is low and coherence is high and energy is sufficient
	•	\kappa_t increases when sustained prediction error or inescapable harm or social defeat patterns occur

Example:

\mu_t = \sigma\!\left(a_0 + a_1 \hat C_t - a_2 \hat H_t + a_3 u_t\right)
\kappa_t = \sigma\!\left(b_0 + b_1 \hat H_t + b_2 \varepsilon_t - b_3 u_t\right)

(\sigma is logistic.)

These are deliberately bland and interpretable.

⸻

What you get from this math
	•	AA: fast situation → mode prior
	•	PCM: commits with hysteresis (prevents thrashing)
	•	μ/κ: opponent modulators controlling both
	•	belief entropy (temperature)
	•	switching inertia (commitment cost)
	•	Control plane: sets precision, learning rate, horizon → shapes E3 selection

This is enough to start implementing and to map pathological regimes (anhedonia, chronic stress, mania-like mode-lock) as parameter failures.

⸻

Abstracted language (your formal-logic layer)

Entities
	•	M=\{m_1..m_K\} modes
	•	AA (AmygdalaAnalogue)
	•	PCM (PreCommitmentModeManager)
	•	E3 (TrajectorySelector)
	•	\mu,\kappa (ValenceGainOverlays)

Streams
	•	z latent(state)
	•	u interoception/energy
	•	s social-context
	•	\varepsilon uncertainty/error
	•	b threat/harm-features

Core relations
	•	AA: (z,u,s,\varepsilon,b)\rightarrow \ell(M)
	•	\tau = \tau_0 \cdot \exp(\alpha_\kappa\kappa-\alpha_\mu\mu)
	•	q = softmax(\ell/\tau)
	•	I'=\lambda I + \eta_\mu\mu-\eta_\kappa\kappa
	•	PCM: (q,I,\Gamma,\theta)\rightarrow c\in M
	•	CP(c)\rightarrow (\Pi,\eta,T)
	•	E3: (\Pi,\eta,T,z)\rightarrow \tau^\*

Meaning
	•	\mu\uparrow \Rightarrow entropy↓, switching↓, commitment↑
	•	\kappa\uparrow \Rightarrow entropy↑, switching↑, re-evaluation↑

⸻

Footnotes
	1.	I used a soft mode belief + hard committed mode split because it matches how you’ve been thinking about “pre-commitment” and avoids brittle discrete switching.
	2.	Treating μ/κ analogues as temperature + inertia is a compact way to express “settling vs destabilising” without inventing a scalar “reward.”
	3.	The separation AA proposes / PCM commits is intentionally analogous to fast salience bias vs stable regime maintenance, and gives you a clear implementable interface between modules.
