# Human relational memory requires time and sleep (Ellenbogen et al., 2007)

Fifty-six participants learned five premise pairs -- A>B, B>C, C>D, D>E, E>F -- with an embedded
hierarchy they were never told about. They were then tested after 20 minutes, after 12 hours
spanning sleep, after 12 hours spanning wake, or after 24 hours. Two things were measured: how
well they retained the pairs they had actually been taught, and how well they could judge pairs
they had never seen (B>D, C>E, B>E), which requires binding the premises into a single ordering.

The trained pairs did nothing interesting. Retention sat above 85% in every group with no
differences between them. The inference pairs did everything: at 20 minutes performance was 52%,
indistinguishable from chance, and after 12 or 24 hours it was above 75% (P < 0.001). The
sleep-specific effect was narrower still -- it appeared on the most distant inference, B>E, at 93%
after sleep against 69% after wake (P = 0.03). Participants' subjective confidence did not track
any of this.

I read this as the cleanest biological statement of the bind INV-063 leg B has walked into. We
have been asking whether a sleep pass improves the world-forward model and answering with a
per-element reconstruction error over the material the pass was trained on. Ellenbogen's premise
pairs are that measure, and they are flat -- not flat because nothing happened, but flat because
they were at ceiling, sitting at a degenerate value in precisely the sense requirement (i) was
written to forbid. Had the study reported only premise-pair retention, the honest conclusion would
have been that sleep does nothing to relational memory, and the inference probe shows that
conclusion to be false. The measure that answered the question was defined over material the
training never touched, and its sensitivity grew with distance from the trained items.

What it does not license is worth stating plainly, because the temptation runs the other way. Most
of the inference gain here belongs to elapsed offline time, not to sleep: the 12-hour wake group
also improved, and only the greatest relational distance carried a sleep-specific advantage. INV-063
leg B asks for an across-sleep delta, and this paper properly supports a weaker claim -- that an
offline period improves held-out relational structure, with a sleep-graded component at the
extreme. A REE run claiming a sleep-attributable gain would need a matched offline-without-sleep
arm that the current four-arm ladder does not carry. Nor does any of this tell us which statistic
on agent.e2.world_forward to compute; it constrains the family, not the member.

Confidence 0.74. The mapping fidelity is unusually high for a cross-domain transfer -- 0.7 -- and
the reason is worth noting, because it is not the usual reason. What transfers here is not a
biological mechanism, which would not survive the trip to a latent forward model at all, but a
finding about measurement design: when a system is trained on one set and probed on another, the
trained-set measure can saturate while the held-out measure carries the entire effect. That is
substrate-independent in a way a circuit claim never is. The transfer risk of 0.45 is driven almost
entirely by the time-versus-sleep decomposition rather than by the species gap.
