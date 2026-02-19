import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/experimental-variogram-1.0.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.0.0" badge="techPreview" />

# variogram

<SchemaUri uri="schema/objects/experimental-variogram/1.0.0/experimental-variogram.schema.json" />

**See also:** [variogram](variogram.md) (fitted model counterpart).

## Overview

The experimental-variogram object is used to capture spatial variability of univariate data acorss an area of interest. Spatial variability is described by direction and summarized per each lag in a direction. 

The experimental variogram is calculated a part of a standard variography workflow and is precursor to variogram modeling. An experimental variogram is a key input to fitting a variogram model.

## Required Data

To construct an experimental variogram object the following information is required.

* `data_variance` (number): The variance of the source data

* `directions` (object): Table describing geometry and type of each direction for which lags exist.
    * `data` (binary blob): Table with columns: offset, count, direction_type, azimuth, dip, azimuth_tolerance, dip_tolerance, bandwidth, bandheight.
        * `offset` (integer): Index in the lags table at which the information associated with this direction begins
        * `count` (integer): Number of entries in lag tabl associated with this direction (number of lags).
        * `direction_type` (string: ["directional", "omnidirectional" or "downhole"]): type of direciton described
        * `azimuth` (float): Clockwise rotation about the z-axis
        * `dip` (float): Incline of the direction, negative points down
        * `azimuth_tolerance` (float): Tolerance considered on either side of the azimuth direction, contributing to the conical definition of the search
        * `dip_tolerance` (float): Tolcerance considered on either side of the dip, contributing to the conical definition of the search
        * `bandwidth` (float): Width of the search to be considered once the conical search has reached its extexts
        * `bandheight` (float): Height of the search to be considered once the conical search has reached its extexts
    * `length` (integer): Number of directions
    * `width` (const): Must be 9
    * `data_type` (const): Must be "uint64/uint64/string/float64/float64/float64/float64/float64/float64"

* `lags` (object): Table describing individual lags
    * `data`(binary blob): Table with columns: start, end, centroid, value, num_pairs.
        * `start` (float): start distance of the lag
        * `end` (float): end distance of the lag
        * `centroid` (float): average distance (centroid) of all pairs represented in lag
        * `value` (float) : calculated value representing spatial correlation, semi-variance or other described by the `variogram_type` field.
        * `num_pairs` (integer): number of pairs considered in the `value` calculation.
    * `length` (integer): Total number of lag bins
    * `width` (const): Must be 5
    * `data_type` (const): Must be "uint64/uint64/float64/float64/float64/float64/uint64"
    * `directions` (object): Contains:

### Example Tables

Two small examples below demonstrate the defined format of the `directions` and `lags` tables described above.

#### Directions Table


| offset | count | direction_type | azimuth | dip | azimuth_tolerance | dip_tolerance | bandwidth | bandheight |
|:------:|:-----:|:--------------:|:-------:|:---:|:-----------------:|:-------------:|:---------:|:----------:|
|   0    |  20   |  directional   |    0    |  0  |       22.5        |     22.5      |    50     |     50     |
|  20    |  20   |  directional   |   90    |  0  |       22.5        |     22.5      |    50     |     50     |
|  40    |  20   |  directional   |    0    | -90 |       10.0        |     10.0      |    20     |     20     |


#### Lags Table


start | end | centroid | value | num_pairs
:--: | :--: | :--: | :--: | :--:
0.0 | 5.0 | 2.5 | 0.012993 | 33
5.0 | 10.0 | 7.5 | 0.160659 | 63
10.0 | 15.0 | 12.5 | 0.313465 | 12
15.0 | 20.0 | 17.5 | 0.422976 | 43
20.0 | 25.0 | 22.5 | 0.502526 | 74

## Optional fields include:

* `description` (string)
* `domain` (string): The domain the variogram is calculated for
* `attribute` (string): The attribute the variogram is calculated for
* `variogram_type` (string, default: "variogram"): Type of calculation performed Both lags and directions can also 
have optional additional attributes through the  attribute-list-property component.
* `distance_unit` (string): Distance units used to describe `start`, `end` and `centroid` in lag table
* `attribute_unit` (string): Units of the attribute being described

The schema enforces unevaluatedProperties: false, meaning no additional properties beyond those defined are allowed.

## Properties

<FlatProperties />

::mermaid[../generated/uml/experimental-variogram-1.0.0.mmd]
