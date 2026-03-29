# A Hierarchy of Temporal Receptive Windows in Human Cortex

**Hasson et al. (2008) -- Journal of Neuroscience**

## What the paper did

Uri Hasson and colleagues introduced the concept of temporal receptive windows (TRWs) -- the duration of the past period over which sensory information influences a neural area's current response. Using fMRI, subjects watched silent films presented forward, backward, or temporally scrambled at different granularities. By measuring how each cortical area's response reliability changed as a function of whether local temporal structure was preserved or disrupted, the authors could estimate each area's characteristic TRW. Areas with short TRWs (early visual cortex, area MT+) responded reliably regardless of whether temporal structure was preserved, because they only need a brief window of input to drive their response. Areas with long TRWs (superior temporal sulcus, precuneus, temporal-parietal junction) showed dramatically reduced reliability when temporal context was disrupted at fine timescales, because they depend on accumulated context to generate a stable response.

## Key findings relevant to SD-008

The paper establishes two things that directly bear on SD-008. First, the temporal integration constant of a neural representation is a functionally meaningful parameter -- it determines what timescale of information drives the current response. This is not a trivial point: the finding demonstrates that the brain has specifically tuned different areas to different TRWs based on their functional role. Second, areas with long TRWs are poor at tracking momentary events: their response depends on accumulated context rather than the immediate input. This is exactly the failure mode that SD-008 corrects. With alpha=0.3, LatentStack's EMA gives z_world a TRW of approximately 3 to 5 timesteps -- it responds to a moving weighted average of recent inputs rather than the current event. Hasson's framework would classify this as a long-TRW unit, appropriate for contextual integration but inappropriate for event detection. Raising alpha to >= 0.9 contracts the TRW to approximately 1 to 2 timesteps, recasting z_world as a short-TRW unit whose response is primarily driven by the most recent input -- appropriate for an area whose job is to detect abrupt environmental events like hazard onset.

## Mapping to REE

In REE's architecture, different processing stages have different temporal scales by design. E1 (LSTM) is intentionally a long-TRW unit: it accumulates experience over many timesteps to build a slow world model, analogous to Hasson's high-order areas. z_world, by contrast, is intended to be event-responsive -- a mid-level feature that E1 and E3 can use to detect when something has changed in the environment. SD-008 is essentially a TRW assignment: z_world is declared to be a short-TRW representation. The Hasson framework provides the neuroscientific rationale for why TRW assignment matters and why using the wrong integration constant for a given functional stage corrupts the computation that stage is supposed to perform.

## Limitations and caveats

The TRW concept maps onto EMA alpha conceptually but not quantitatively. Hasson's TRWs are measured in seconds (from sub-second in early visual areas to multi-second in high-order cortex), while REE's timestep duration and the exact value 0.9 are not derivable from this framework alone. The mapping is also directional rather than mechanistic: the paper does not model an EMA filter and does not study event detection failure specifically. Additionally, Hasson's hierarchy is about distinct anatomical areas with different structural connectivity, not about tuning parameters within a single module. The SD-008 threshold of 0.9 comes from REE-specific experimental evidence (EXQ-023, EXQ-040), not from this paper.

## Confidence reasoning

The Hasson paper is high quality -- published in Journal of Neuroscience, widely cited, and the TRW concept is now canonical in systems neuroscience. The mapping to SD-008 is conceptually clean: the paper establishes why integration constant matters for event responsiveness, which is exactly what SD-008 is about. Confidence is set at 0.72 -- high enough to count as meaningful support but moderated by the quantitative gap between TRW-in-seconds and alpha-in-discrete-timesteps, and by the structural difference between area-level TRW assignment and module-level parameter tuning.
