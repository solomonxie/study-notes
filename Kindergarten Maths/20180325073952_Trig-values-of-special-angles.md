# Trig values of `special angles`
> `Trig values` refer to Trigonometric values such as `Sine/Cosine/Tangent values`.
`Special angles` refer to **0°, 30°, 45°, 60°** 

[Easier way: refer to `unit circle`.](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-377953990)

The follow are to remember in mind:

- `0°` (or `0 Radians`):
```py
sin(0°) = 0
cos(0°) = 1
```
- `30°` (or `π/6 Radians`):
```py
sin(30°) = cos(60°) = 1/2
cos(30°) = sin(60°) = √3/2
```
- `45°` (or `π/4 Radians`):
```py
sin(45°) = cos(45°) = √2/2
```
- `60°` (or `π/3 Radians`):
```py
sin(60°) = cos(30°) = √3/2
cos(60°) = sin(30°) = 1/2
```

## `Trig Identities`
Definition as below:

```py
sin(θ) = - sin(-θ)
cos(θ) = + cos(-θ)

sin(θ) = - sin(360° - θ)
cos(θ) = + cos(360° - θ)

sin(θ) = + sin(180° - θ)
cos(θ) = - cos(180° - θ)

sin(θ) = - sin(180° + θ)
cos(θ) = - cos(180° + θ)
```

Example, by using the identities, we could easily calculate a bunch of big angles:
```py
sin(315°) = sin(360° - 45°) = - sin(45°) = - √2/2
cos(315°) = cos(360° - 45°) = cos(45°) = √2/2
```
