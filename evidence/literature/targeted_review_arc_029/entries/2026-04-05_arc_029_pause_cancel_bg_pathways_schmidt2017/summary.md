# Summary: Schmidt & Berke 2017 -- Pause-then-Cancel model of BG stopping

**Citation:** Schmidt R, Berke JD. "A Pause-then-Cancel model of stopping: evidence from basal ganglia neurophysiology." Philosophical Transactions of the Royal Society B: Biological Sciences. 2017;372(1718). DOI: 10.1098/rstb.2016.0202. PMID: 28242736. (PubMed)

---

## What the paper shows

Schmidt & Berke review BG neurophysiology evidence to argue that action stopping involves two separable processes, not a single Stop signal:

1. **Pause**: Rapid, stimulus-unspecific pause in action execution, mediated by brief beta oscillations in striatum and STN hyperdirect pathway activation. Covers all current action programs; fast but non-selective.

2. **Cancel**: Selective cancellation of the specific action program that should not be executed, mediated by arkypallidal neurons from GPe to striatum. Slower but action-specific.

The key contribution: distinct BG cell types and pathways implement distinct sub-processes. The beta oscillation epochs in striatum specifically correspond to the Pause state -- a temporary hold on committed execution.

Implications for speed-accuracy trade-offs: the Pause mechanism buys time for the Cancel process to arrive, allowing stopping to succeed more often without requiring either to be maximally fast.

---

## Relevance to ARC-029

ARC-029 predicts that committed-mode operation (BetaGate elevated) produces lower harm rates. The Pause-then-Cancel framework provides mechanistic grounding:

1. **Commit threshold = Pause/Cancel decision**: The moment an agent commits to an action corresponds to the moment when Pause evaluation completes without triggering Cancel. In REE terms: the BetaGate threshold gates whether the Pause resolves to commit or to cancel.

2. **Committed mode = post-Pause protected execution**: Once the Pause window closes without Cancel, the action enters committed-mode execution via the direct pathway. This is the operational regime where ARC-029 predicts lower harm -- because the Pause phase has already screened out the most dangerous impulses.

3. **Uncommitted mode = elevated Pause probability**: Agents that frequently re-enter Pause evaluation (uncommitted mode) have higher variance in execution and higher probability of mistimed or incomplete action programs that encounter hazards.

4. **Distinct neural pathways = distinct operational modes**: The paper's core contribution is that Go, Pause, and Cancel map to distinct BG circuitry. This directly supports ARC-029's architectural claim that committed and uncommitted modes are not a continuum but discrete operational states with different neural implementations.

---

## Limitations for REE mapping

- The Pause-then-Cancel framework describes per-trial events, not sustained operational regimes across trajectories
- The paper focuses on the stopping pathway; ARC-029's committed-mode benefit is about staying-committed
- Harm rate is not directly measured in stop-signal tasks -- error rate (failure to cancel) is the proxy
- The review synthesizes existing data; not primary evidence

---

## Evidence verdict

**Supports ARC-029** (confidence: 0.65). The Pause-then-Cancel model provides mechanistic evidence that the commit threshold is implemented by distinct BG circuitry (beta Pause + arkypallidal Cancel), and that committed execution is a distinct state with its own neural signature. This supports the architectural separability claim within ARC-029 and provides a mechanism for why committed-mode operation would have lower reactive-exploration harm.
