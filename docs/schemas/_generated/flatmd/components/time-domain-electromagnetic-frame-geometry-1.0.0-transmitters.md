### time-domain-electromagnetic-frame-geometry (v1.0.0)

| Property | Type | Description | Flags |
|---|---|---|---|
| id | Integer | Transmitter identifier. | ✅ |
| center | coordinates-3d | The center of the first transmitter coil, is the origin of the geometry. First transmitter: 0,0,0 Although it is not necessary to supply the origin of the first transmitter, it is declared as mandatory to eliminate potential ambiguity about the origin of the additional transmitters. For multiple transmitter coils, the offset of the center of each transmitter is relative to the first transmitter. Z axis is positive up (left-handed coordinate system). | ✅ |
| direction | String | Transmitter loop orientation. | ✅ |
| area | Number | This is the actual transmitter area.  The effective area is TXnAREA * TXnTURNS (m^2) | ✅ |
| node_coordinates | Array[coordinates-3d] | Node coordinates, Set of x,y,z coordinates relative to the first transmitter. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

