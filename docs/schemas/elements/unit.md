import SchemaUri from '@theme/SchemaUri';

# unit

<SchemaUri uri="schema/elements/unit/1.0.1/unit.schema.json" />

Defines physical measurement units as a string enum with 125+ supported unit categories, each corresponding to a physical dimension. Components that describe measured quantities (e.g., distances, temperatures, pressures) reference this element to specify their unit of measure.

The categories are organised by physical dimension:

### Dimensionless and ratios

- `unit-dimensionless` — quantities with no physical dimension
- `unit-non-dimensional` — non-dimensional ratios and coefficients

### Geometry and spatial

- `unit-length` — linear distance (metres, feet, etc.)
- `unit-area` — two-dimensional extent
- `unit-volume` — three-dimensional extent
- `unit-reciprocal-length` — inverse length (e.g., wavenumber)
- `unit-reciprocal-area` — inverse area
- `unit-reciprocal-volume` — inverse volume
- `unit-plane-angle` — angles in a plane (degrees, radians, etc.)
- `unit-solid-angle` — solid angles (steradians)
- `unit-angle-per-length` — angular change per unit length
- `unit-angle-per-volume` — angular change per unit volume
- `unit-length-per-temperature` — thermal expansion coefficient (length)
- `unit-length-per-mass` — length per unit mass
- `unit-length-per-pressure` — length per unit pressure
- `unit-second-moment-of-area` — second moment of area (moment of inertia of a cross-section)

### Time and motion

- `unit-time` — duration (seconds, hours, etc.)
- `unit-reciprocal-time` — inverse time (frequency)
- `unit-length-per-time` — velocity
- `unit-linear-acceleration` — rate of change of velocity
- `unit-angular-velocity` — rate of angular change
- `unit-angular-acceleration` — rate of change of angular velocity
- `unit-time-per-length` — slowness (inverse velocity)
- `unit-time-per-volume` — time per unit volume
- `unit-time-per-mass` — time per unit mass
- `unit-volume-per-rotation` — displacement volume per revolution

### Mass and density

- `unit-mass` — quantity of matter (kilograms, pounds, etc.)
- `unit-reciprocal-mass` — inverse mass
- `unit-reciprocal-mass-time` — inverse mass-time product
- `unit-mass-per-length` — linear density
- `unit-mass-per-area` — areal density
- `unit-mass-per-volume` — volumetric density
- `unit-mass-per-volume-per-length` — density gradient
- `unit-mass-per-time` — mass flow rate
- `unit-mass-per-time-per-area` — mass flux
- `unit-mass-per-time-per-length` — dynamic viscosity
- `unit-mass-per-energy` — mass per unit energy
- `unit-mass-length` — mass-length product (first moment of mass)
- `unit-mass-per-amount-of-substance` — molar mass
- `unit-volume-per-mass` — specific volume
- `unit-area-per-mass` — mass absorption coefficient
- `unit-length-per-mass` — length per unit mass

### Force and pressure

- `unit-force` — force (newtons, pounds-force, etc.)
- `unit-reciprocal-force` — inverse force
- `unit-force-per-volume` — body force density
- `unit-force-area` — force-area product
- `unit-momentum` — linear momentum
- `unit-reciprocal-pressure` — compressibility
- `unit-pressure-squared` — pressure squared
- `unit-pressure-per-volume` — pressure gradient per volume
- `unit-pressure-time-per-volume` — pressure-time per volume
- `unit-volume-per-pressure` — volume per unit pressure
- `unit-length-per-pressure` — length per unit pressure

### Energy and power

- `unit-energy` — energy (joules, calories, etc.)
- `unit-energy-per-time` — power
- `unit-energy-per-mass` — specific energy
- `unit-energy-per-mass-per-time` — specific power
- `unit-energy-per-volume` — energy density
- `unit-energy-per-area` — energy per unit area
- `unit-molar-energy` — energy per amount of substance
- `unit-moment-of-inertia` — rotational inertia
- `unit-power-per-area` — power flux (irradiance)
- `unit-power-per-volume` — volumetric power density

### Temperature and thermal

- `unit-thermodynamic-temperature` — absolute temperature (kelvin, rankine)
- `unit-temperature-difference` — temperature difference
- `unit-reciprocal-temperature` — inverse temperature
- `unit-temperature-interval-per-length` — temperature gradient
- `unit-temperature-interval-per-time` — rate of temperature change
- `unit-temperature-interval-per-pressure` — Joule–Thomson coefficient
- `unit-thermal-resistance` — thermal resistance
- `unit-thermal-insulance` — thermal insulance (R-value)
- `unit-thermal-conductance` — thermal conductance
- `unit-thermal-conductivity` — thermal conductivity
- `unit-specific-heat-capacity` — specific heat capacity
- `unit-heat-capacity` — heat capacity
- `unit-molar-heat-capacity` — molar heat capacity
- `unit-heat-transfer-coefficient` — convective heat transfer coefficient
- `unit-volumetric-heat-transfer-coefficient` — volumetric heat transfer coefficient

### Electrical and magnetic

- `unit-electric-current` — electric current (amperes)
- `unit-electric-current-density` — current per unit area
- `unit-electric-charge` — electric charge (coulombs)
- `unit-electric-charge-per-area` — surface charge density
- `unit-electric-charge-per-volume` — volume charge density
- `unit-electric-charge-per-mass` — charge-to-mass ratio
- `unit-electric-potential-difference` — voltage (volts)
- `unit-reciprocal-electric-potential-difference` — inverse voltage
- `unit-electric-resistance` — electrical resistance (ohms)
- `unit-electric-resistance-per-length` — resistance per unit length
- `unit-electrical-resistivity` — electrical resistivity
- `unit-electric-conductance` — electrical conductance (siemens)
- `unit-electric-conductivity` — electrical conductivity
- `unit-electric-field-strength` — electric field strength
- `unit-capacitance` — capacitance (farads)
- `unit-permittivity` — dielectric permittivity
- `unit-inductance` — inductance (henries)
- `unit-magnetic-field-strength` — magnetic field strength (H-field)
- `unit-magnetic-flux` — magnetic flux (webers)
- `unit-magnetic-flux-density` — magnetic flux density (teslas)
- `unit-magnetic-flux-density-per-length` — magnetic flux density gradient
- `unit-magnetic-permeability` — magnetic permeability
- `unit-magnetic-vector-potential` — magnetic vector potential
- `unit-magnetic-dipole-moment` — magnetic dipole moment
- `unit-electromagnetic-moment` — electromagnetic moment
- `unit-dipole-moment` — electric dipole moment
- `unit-reluctance` — magnetic reluctance

### Optical and photometric

- `unit-luminous-intensity` — luminous intensity (candelas)
- `unit-luminance` — luminance
- `unit-luminous-flux` — luminous flux (lumens)
- `unit-illuminance` — illuminance (lux)
- `unit-quantity-of-light` — quantity of light (lumen-seconds)
- `unit-light-exposure` — light exposure (lux-seconds)
- `unit-luminous-efficacy` — luminous efficacy
- `unit-radiant-intensity` — radiant intensity
- `unit-radiance` — radiance

### Chemistry and amount of substance

- `unit-amount-of-substance` — amount of substance (moles)
- `unit-amount-of-substance-per-area` — surface concentration
- `unit-amount-of-substance-per-volume` — molar concentration
- `unit-amount-of-substance-per-time` — molar flow rate
- `unit-amount-of-substance-per-time-per-area` — molar flux
- `unit-area-per-amount-of-substance` — molar area
- `unit-molar-volume` — molar volume

### Flow and volume rates

- `unit-volume-per-time` — volumetric flow rate
- `unit-volume-per-time-per-time` — rate of change of volumetric flow
- `unit-volume-per-time-length` — volumetric flow per unit length
- `unit-volume-per-time-per-pressure` — productivity index
- `unit-volume-per-time-per-pressure-length` — transmissibility
- `unit-area-per-time` — kinematic viscosity / diffusivity

### Currency

- `unit-currency` — monetary value

For the complete list of supported unit strings within each category, refer to the schema source.
