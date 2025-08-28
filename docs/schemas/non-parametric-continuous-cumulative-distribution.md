import CheckIcon from '@mui/icons-material/Check';
import Chip from '@mui/material/Chip';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/non-parametric-continuous-cumulative-distribution-1.2.0.md';

# non-parametric-continuous-cumulative-distribution

<Chip color="info" icon={<CheckIcon />} label="Supported" /><br />
<SchemaUri uri="schema/objects/non-parametric-continuous-cumulative-distribution/1.2.0/non-parametric-continuous-cumulative-distribution.schema.json" />

The non-parametric-continuous-cumulative-distribution object captures the statistical cumulative distribution function (CDF) of a property. It is non-parametric since the CDF is not characterized by a known distribution (e.g., normal or lognormal) or by a mathematical formula. Instead, the cumulative probability is calculated directly from the data and from an extrapolation function if the data does not capture the full range of possible values.

This schema is particularly useful in geostatistics where the distribution of properties such as mineral grades, porosity, or seismic velocities may not follow a known distribution. This object is beneficial for geostatistical conditional simulations, change of support analysis and other methods that typically assume Gaussianity, though natural data is rarely follow a Gaussian distribution. Techniques like declustering and Gaussian anamorphosis help manage these distributions, where Gaussian anamorphosis does not assume a predefined distribution, but instead, it derives a transformation function from the empirical (non-parametric) CDF, ensuring a data-driven approach.

To create this object, the user must provide:

- The pairs of values and probabilities. Note that the values are sorted and the probabilities should be monotonically increasing between 0 and 1 (excluded).
- The lower tail extension; use No_extrapolation if the lowest value is also the minimum of the distribution.
- The upper tail extension; use No_extrapolation if the largest value is also the maximum of the distribution.
- Note the support of the distribution. Select Point or specify a block size.
- Specify if the distribution has been declustered.

## Properties

<FlatProperties />

::mermaid[_generated/uml/non-parametric-continuous-cumulative-distribution-1.2.0.mmd]
