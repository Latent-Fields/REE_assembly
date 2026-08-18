# Chinchilla: the baseline scales proportionally, and unmatched comparisons invert

Hoffmann and colleagues trained over 400 language models from 70M to 16B parameters on 5B to
500B tokens to find where the compute-optimal frontier actually lies. The answer was that model
size and training tokens should scale *equally*: double the parameters, double the tokens. On
that basis they trained Chinchilla — 70B parameters, four times Gopher's data, the same compute
budget — and it beat Gopher (280B), GPT-3 (175B), Jurassic-1 (178B) and Megatron-Turing NLG
(530B) across a wide evaluation range.

I have marked this `mixed` rather than `supports`, because it genuinely does two opposing jobs
for Q-093 and collapsing them into one direction would be dishonest.

The supporting job is methodological, and it is the strongest warrant available for the
non-degeneracy precondition Q-093 writes into its own `what_would_answer`. Chinchilla's entire
result exists because someone re-ran the comparison at *equal compute* instead of equal
parameter count — and the ranking inverted. A 70B model beat a 530B one. That is not a
cautionary tale about weaker evidence; it is a demonstration that comparisons made at
unmatched budget can be rank-reversing, which means a REE-versus-baseline efficiency claim
asserted at unmatched competence would be worthless rather than provisional. Q-093 already
says this. Chinchilla is why it is right to say it.

The opposing job is substantive. For monolithic transformers — the comparison class REE would
be measured against — capacity and experience scale strictly 1:1. There is no sublinear
dividend sitting in the baseline waiting to be claimed. Whatever efficiency advantage REE has
must therefore come from the architectural seam between control machinery and representational
store, because the baseline class already sits on its own optimum. That sharpens Q-093
considerably: it converts a vague "is REE more efficient" into "does the control/representation
seam buy something that a well-tuned monolith cannot get by tuning".

Two limits keep the confidence at 0.66 despite near-maximal source quality. Chinchilla's
parameter count N is undecomposed — a monolithic transformer has no control-versus-store seam
at all, so this paper cannot measure Q-093's ratio in the baseline, only an aggregate. And its
cost axis is pre-training FLOPs alone, a strict subset of Q-093's lifetime-cost definition;
importing the 1:1 rule as "the baseline scaling law" into a REE comparison would compare unlike
denominators. There is also a temptation worth naming and refusing: this result describes the
compute-optimal *frontier*, and most real deployed systems sit off it. Beating an off-frontier
baseline would be easy and would prove nothing.
