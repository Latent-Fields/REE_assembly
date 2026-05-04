# SD-049 Phase 2 encoder identity-expansion verdict

**Decision:** **Option C (hybrid)** — phased shared-backbone-split-heads architecture.

**Confidence:** 0.78

**Verdict-shaping question:** does z_resource carry resource-type identity as (A) a one-hot identity slot concatenated with magnitude latent, (B) a low-D learned embedding capturing similarity structure across types, or (C) a hybrid where one-hot identity is the supervision target and a learned-embedding substrate provides similarity structure underneath?

---

## Recommendation

Implement option C (hybrid) for Phase 2 with the following concrete shape:

- **Shared trunk:** an MLP encoder taking `world_obs` and producing a 32-dim latent representation. This is the distributed similarity-preserving substrate (the monosynaptic-analog from Schapiro 2017; the substrate that distributes-and-similarity-preserves per Schapiro 2016 / Howard 2015 distributed-pattern coding).
- **Identity-classifier head:** a small linear head trained during phase P0 on `obs_dict["resource_type_at_agent"]` (one-hot supervision). This is the labeled-line read-out (the trisynaptic-analog from Schapiro 2017; the per-population identity coding from Ballesta-Padoa-Schioppa 2019; the sparse explicit code from Quiroga 2005).
- **Magnitude / proximity head:** the existing SD-015 `resource_prox_head` continues unchanged.
- **z_resource output:** concatenation of the trunk embedding (similarity-rich) and the identity-classifier logits / one-hot prediction (labeled-line). Downstream consumers can read whichever fits their needs.

This shape is biologically the most faithful (the bi-pathway architecture Schapiro 2017 directly licenses) and addresses both the V3-EXQ-514 identity-recovery acceptance criterion (via the classifier head) and the wanting/liking similarity-structure requirement (via the embedding trunk).

---

## Strongest 2–3 findings per branch

### Option A (one-hot identity slot + magnitude latent)

1. **Ballesta & Padoa-Schioppa 2019** ([10.1016/j.cub.2019.09.027](https://doi.org/10.1016/j.cub.2019.09.027)): macaque OFC neurons encode good identities and values in a juice-based labeled-line representation -- distinct neural populations encode distinct juice identities, with within-population firing-rate coding of value. This is the cleanest biological precedent for option A's shape.
2. **Quiroga et al. 2005** ([10.1038/nature03687](https://doi.org/10.1038/nature03687)): human MTL concept cells produce sparse, invariant, explicit identity readouts. The architectural shape (sparse one-cell-per-identity readout) matches option A's supervision target.
3. **Engineering counter-argument:** option A is collapse-immune by construction. No embedding to collapse -> no risk of class collapse (Levi et al. 2021).

### Option B (learned low-D embedding)

1. **Schapiro et al. 2016** ([10.1002/hipo.22523](https://doi.org/10.1002/hipo.22523)): human hippocampus learns higher-order temporal community structure; representations within the same community become more similar after exposure. This requires distributed similarity-preserving substrate and is structurally inconsistent with labeled-line-only architectures.
2. **Howard et al. 2015** ([10.1073/pnas.1503550112](https://doi.org/10.1073/pnas.1503550112)): identity-specific predictive representations in lateral OFC are MVPA-decodable from distributed activity patterns. Pattern-based coding is more naturally option B than option A.
3. **Engineering hazard:** Levi et al. 2021 ([10.48550/arXiv.2006.05162](https://doi.org/10.48550/arXiv.2006.05162)) document the canonical class-collapse failure mode under metric-learning-style training. Option B's Phase 2 implementation must include explicit anti-collapse mechanisms.

### Option C (hybrid)

1. **Schapiro et al. 2017** ([10.1098/rstb.2016.0049](https://doi.org/10.1098/rstb.2016.0049)): the architectural-resolution paper. Hippocampus reconciles labeled-line per-instance coding with distributed similarity-preserving coding by having BOTH pathways: monosynaptic for statistical learning, trisynaptic for episode-specific pattern separation. This is direct biological licensing for option C.
2. **Howard et al. 2015** (cross-tag): the lateral-OFC-vs-vmPFC dissociation suggests parallel substrates for identity-specific (option A's labeled-line shape) and identity-general (option B's distributed shape) representations. Two substrates, two roles.
3. **Convergent reading of the slate:** Quiroga + Ballesta favour option A at the readout end; Schapiro 2016 + Howard favour option B at the substrate end. Schapiro 2017's bi-pathway architecture is the synthesis.

---

## Why option C wins (and the trade-offs)

### Biological grounding

The slate splits cleanly: option A has strong biological support at the *readout* end (concept cells, OFC labeled lines), but Schapiro 2016 + Howard 2015 + Schapiro 2017 collectively argue that the *substrate* producing those readouts is distributed-and-similarity-preserving. The biology is bi-pathway. Option C is the architectural translation.

### Phase 2 acceptance criteria

V3-EXQ-514 has two criteria that pull in different directions:

- Identity-recovery accuracy > 0.6 in ARM_2 (linear probe on z_resource): naturally suited to a labeled-line readout (option A's strength).
- Wanting != liking trajectory dissociation >= 0.6 in ARM_2 + per-axis drive ANOVA on z_goal cluster IDs p < 0.01: requires similarity-rich representation across types (option B's strength).

Option A passes the first cleanly but may underfit the second; option B inverts the trade-off; option C addresses both.

### Engineering cost

Option C is more expensive than option A (embedding trunk + classifier head + magnitude head) but not much more expensive than option B (which already needs phased training to defend against class collapse per Levi et al. 2021). The Phase 2 phased training protocol already specified in `substrate_queue.json` (P0 frozen identity-classifier head -> P1 joint -> P2 eval) is naturally suited to option C: P0 trains the classifier head while the trunk is randomly initialised; P1 jointly trains trunk + classifier; P2 evaluates both. The classifier head provides the supervised anti-collapse signal that option B alone would need to add separately.

The cost over option A is moderate (one extra head + classifier loss term), and the architectural pay-off is biological grounding plus dual-objective acceptance handling. Net recommendation: option C.

---

## Falsifier branch for V3-EXQ-514 ARM_2

If Phase 2 lands as option C and ARM_2 still fails to produce `goal_resource_r >= 0.5` or `wanting_target != liking_target` trajectory fraction >= 0.6, the diagnostic is structured as follows (each row maps a distinct failure to a distinct architectural conclusion):

| Failure mode | Diagnostic signature | Architectural reading |
|---|---|---|
| Identity-recovery PASS, wanting!=liking FAIL | Classifier head learned identity from one-hot supervision, but trunk embedding did not develop similarity structure | Option C trunk under-trained: extend P0 / increase auxiliary similarity loss weight; do NOT fall back to option A (would regress wanting!=liking further). |
| Identity-recovery FAIL, wanting!=liking PASS | Trunk learned similarity but classifier head collapsed | P0 head freezing did not stick; revisit phased-training boundaries. Option B-only fallback is viable but fails identity criterion. |
| Both FAIL with high embedding norm variance | Class collapse on the trunk per Levi et al. 2021 | Add adaptive same-class positive sampling; or fall back to option A with explicit cross-type discriminability test. |
| Both FAIL with flat trunk activations | Trunk capacity bottleneck or learning-rate mismatch | Standard hyperparameter search; not architectural. |
| Both PASS but with degenerate goal_resource_r profile | Classifier dominates trunk read-out | Fix concatenation order or add gating between heads. |
| Both FAIL across ARM_2 AND ARM_3 | Substrate incapable regardless of architecture | Phase 1 substrate insufficient; reopen Phase 1 substrate (this is the Woo/Spelke-style falsifier branch -- routes MECH-229 to substrate_conditional with V4-1 multi-agent ecology dependency). |

The hybrid-architecture-licensed-by-Schapiro-2017 verdict is robust to most Phase 2 failure modes -- they map onto specific implementation hazards rather than architectural error. Only the last row (joint failure across both arms with identical structure) would re-open the Phase 1 substrate question, and that is the same falsifier branch the SD-049 design doc already specifies.

---

## What this lit-pull does NOT settle

1. **The specific concatenation / read-out interface for option C.** The verdict commits to shared-trunk + classifier-head + magnitude-head, but not to how downstream consumers (E3 evaluation, GoalState seeding, MECH-295 liking-bridge) read the concatenated z_resource. That is Phase 2 implementation work; the lit-pull licenses the architecture but not the wiring details.
2. **Whether to use contrastive vs supervised auxiliary losses on the trunk.** The trunk embedding has to be shaped somehow during P0/P1. Supervised auxiliary loss on resource-type identity (cross-tag with the classifier head) is the simplest and engineering-safest. Contrastive supervision would shape similarity structure more explicitly but adds loss-design complexity. Default: supervised aux loss on the trunk during P0, with a similarity-preserving auxiliary objective (e.g. cross-type cosine similarity penalty) added during P1. This decision can be deferred to Phase 2 implementation review.
3. **The right number of resource types for ARM_2.** The lit-pull does not adjudicate whether 3 types is biologically sufficient for the wanting/liking dissociation MECH-229 cares about. The SD-049 design doc validation experiment treats 3-type as the default and 5-type as overshoot; this verdict accepts that framing.

---

## Cross-tag summary

| Entry | Direction | Confidence | Tags |
|---|---|---|---|
| Quiroga 2005 | supports option A | 0.82 | sd_049, sd_015, mech_229 |
| Ballesta & Padoa-Schioppa 2019 | supports option A | 0.83 | sd_049, sd_015, mech_229, mech_230 |
| Howard et al. 2015 | mixed (option B/C) | 0.79 | sd_049, sd_015, mech_229, mech_230 |
| Schapiro et al. 2016 | weakens option A | 0.78 | sd_049, sd_015, mech_229, mech_230 |
| Schapiro et al. 2017 | supports option C (hybrid) | 0.82 | sd_049, sd_015, mech_229, mech_230 |
| Levi et al. 2021 | weakens option B (engineering hazard only) | 0.74 | sd_049, sd_015 |

Net SD-049 lit_conf contribution from this lit-pull: ~0.79 average across 6 entries. Quadrant remains plausible_unproven (still no exp evidence for SD-049 itself; lit_conf rises with the additional entries).

---

## Recommended Phase 2 implementation note

```python
class ResourceEncoder(nn.Module):
    def __init__(self, world_obs_dim, z_resource_dim=32, n_resource_types=3,
                 hidden_dim=64, identity_classifier_enabled=True):
        super().__init__()
        # Shared trunk (Schapiro 2017 monosynaptic-analog; Schapiro 2016 distributed substrate)
        self.trunk = nn.Sequential(
            nn.Linear(world_obs_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, z_resource_dim),
        )
        # Identity-classifier head (Schapiro 2017 trisynaptic-analog;
        # Ballesta-Padoa-Schioppa 2019 labeled lines; Quiroga 2005 sparse readout)
        if identity_classifier_enabled:
            self.identity_head = nn.Linear(z_resource_dim, n_resource_types)
        # Magnitude head (existing SD-015 SD-018 resource_prox_head pattern)
        self.resource_prox_head = nn.Sequential(
            nn.Linear(z_resource_dim, 1), nn.Sigmoid()
        )

    def forward(self, world_obs):
        z_trunk = self.trunk(world_obs)            # similarity-preserving embedding
        identity_logits = self.identity_head(z_trunk)  # labeled-line readout
        resource_prox = self.resource_prox_head(z_trunk)
        # z_resource = concat(trunk, identity_softmax) gives downstream consumers both shapes
        identity_prob = torch.softmax(identity_logits, dim=-1)
        z_resource = torch.cat([z_trunk, identity_prob], dim=-1)
        return z_resource, identity_logits, resource_prox
```

Phased training:
- **P0:** train trunk + classifier head + resource_prox head jointly with cross-entropy on identity tags + MSE on resource proximity, both as auxiliary losses. Anti-collapse: classifier head provides supervised pull on the trunk (Levi 2021 mitigation in spirit).
- **P1:** freeze classifier head; continue training trunk under E1/E3/downstream-task losses. Trunk embedding is allowed to develop similarity structure beyond what classifier supervision alone provides.
- **P2:** evaluate identity-recovery accuracy (linear probe on trunk) AND wanting!=liking trajectory dissociation. Both must pass for the V3-EXQ-514 acceptance.

This is the implementation surface I recommend Phase 2 implement.
