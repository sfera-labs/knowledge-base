# Equivalent Continuous Sound Level (Leq)

The evaluation of the *Equivalent Continuous Sound Level* (*Leq*) represents the cumulative level of the sound/noise energy produced during a specific time period.

Time period and frequency adjustments (weightings) are applied to target specific analysis requirements:

### Time weighting:
- **FAST**: 125ms period. It replicates the natural response of human ear;
- **SLOW**: 1000ms period. It is good at "ignoring" short, fast sounds like car doors slamming or balloons popping. A good choice for environmental noise studies, especially for studies that span many hours or even days;
- **IMPULSE**: 35ms period. It is usually used in situations where there are sharp impulsive noises to be measured, such as fireworks or gun shots.

### Frequency weighting:
- **A**: it replicates the human ear response to different frequency bandwidths;
- **C**: flat response with extreme high (near 20kHz) and low (near 0 Hz) frequencies attenuated;
- **Z**: no frequency adjustments.

If A or C frequency weighting is applied, the sound levels are adjusted according to the values of a specific table with adjustment factors. This table groups the adjustment factors into bandwidths of octaves or fractions of octaves. For instance:

**1 octave weighting table:**
|Frequency [Hz]|A-weighting [dB]|C-weighting [dB]|
|----|:---:|:-:|
|8|-77.8|-17.7|
|16|-56.7|-8.5|
|31.5|-39.4|-3.0|
|63|-26.2|-0,8|
|125|-16.1|-0.2|
|250|-8.6|0.0|
|500|-3.2|0.0|
|1000|0.0|0.0|
|2000|1.2|-0.2|
|4000|1.0|-0.8|
|8000|-1.1|-3.0|
|16000|-6.6|-8.5|

**1/3 octave weighting table:**
|Frequency [Hz]|A-weighting [dB]|C-weighting [dB]|
|----|:---:|:-:|
|6.3|-85.4|-21.3|
|8|-77.8|-17.7|
|10|-70.4|-14,3|
|12.5|-63,4|-11.2|
|16|-56.7|-8.5|
|20|-50.5|-6.2|
|25|-44.7|-4.4|
|31.5|-39.4|-3.0|
|40|-34.6|-2.0|
|50|-30.2|-1.3|
|63|-26.2|-0,8|
|80|-22.5|-0.5|
|100|-19.1|-0.3|
|125|-16.1|-0.2|
|160|-13.4|-0.1|
|200|-10.9|0.0|
|250|-8.6|0.0|
|315|-6.6|0.0|
|400|-4.8|0.0|
|500|-3.2|0.0|
|630|-1.9|0.0|
|800|-0.8|0.0|
|1000|0.0|0.0|
|1250|0.6|0.0|
|1600|1.0|-0.1|
|2000|1.2|-0.2|
|2500|1.3|-0.3|
|3150|1.2|-0.5|
|4000|1.0|-0.8|
|5000|0.5|-1.3|
|6300|-0.1|-2.0|
|8000|-1.1|-3.0|
|10000|-2.5|-4.4|
|12500|-4.3|-6.2|
|16000|-6.6|-8.5|
|20000|-9.3|-11.2|
