/**
 * Copyright © 2025 Bentley Systems, Incorporated
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *     http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

using CsvHelper;
using OSDUUnits;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;

class Program
{
    private const string osdu_schema_version = "1.0.0";
    private const string output_schema_version = "1.0.1";

    static void Main()
    {
        Console.WriteLine("Generating units...");

        using (var reader = new StreamReader($".\\UnitOfMeasure.{osdu_schema_version}.csv"))
        using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
        {
            using (var unit_writer = new StreamWriter(@".\unit.schema.json"))
            {
                unit_writer.WriteLine("{");
                unit_writer.WriteLine($"\t\"$id\": \"/elements/units/{output_schema_version}/unit.schema.json\",");
                unit_writer.WriteLine("\t\"$schema\": \"https://json-schema.org/draft/2020-12/schema\",");
                unit_writer.WriteLine("\t\"description\": \"Units\",");
                unit_writer.WriteLine("\t\"$comment\": \"OSDU Units\",");
                unit_writer.WriteLine("\t\"type\": \"string\",");
                unit_writer.WriteLine("\t\"anyOf\": [");

                var records = csv.GetRecords<Unit>();

                // Add extra units required by BlockSync service and not found in OSDU schema
                var extra_units = new List<Unit>{
                    new Unit { UnitDimensionName = "currency", ID = "$", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "currency", ID = "$/t", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "currency", ID = "$/ton[US]", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "dimensionless", ID = "0.01 ct/t", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "dimensionless", ID = "ct/t", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "dimensionless", ID = "ppb[mass]", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "dimensionless", ID = "oz t/ton[US]", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "dimensionless", ID = "ug/kg", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "mass per volume", ID = "ton[US]/ft3", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "mass", ID = "kt", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "mass", ID = "kton[UK]", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "mass", ID = "kton[US]", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "mass", ID = "Mt", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "mass", ID = "Mton[UK]", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "mass", ID = "Mton[Us]", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "mass", ID = "Mlbm", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "mass", ID = "1000 ct", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "mass", ID = "1000 ozm[troy]", IsOsduUnit = false },
                    new Unit { UnitDimensionName = "mass", ID = "1000000 ozm[troy]", IsOsduUnit = false }
                };

                records = records.Concat(extra_units.AsEnumerable());

                var results = records.GroupBy(x => x.UnitDimensionName);
                
                var currentGroup = 0;
                foreach (var group in results)
                {
                    var all_osdu = group.All(x => x.IsOsduUnit);
                    var any_osdu = group.Any(x => x.IsOsduUnit);
                    var source = all_osdu ? "OSDU Units" : any_osdu ? "OSDU & BlockSync Units" : "BlockSync Units";

                    Directory.CreateDirectory(".\\categories");  // Create output dir if it doesn't exist

                    var name = group.Key.Trim().Replace(' ', '-');
                    using (var writer = new StreamWriter($".\\categories\\unit-{name}.schema.json"))
                    {
                        writer.WriteLine("{");
                        writer.WriteLine($"\t\"$id\": \"/elements/units/{output_schema_version}/categories/unit_{name}.schema.json\",");
                        writer.WriteLine("\t\"$schema\": \"https://json-schema.org/draft/2020-12/schema\",");
                        writer.WriteLine($"\t\"description\": \"Units ({group.Key})\",");
                        writer.WriteLine($"\t\"$comment\": \"{source}\",");
                        writer.WriteLine("\t\"type\": \"string\",");
                        writer.WriteLine("\t\"enum\": [");
                        foreach (var value in group)
                        {
                            writer.Write($"\t\t\"{value.ID}\"");
                            if (value == group.Last())
                                writer.WriteLine();
                            else
                                writer.WriteLine(",");
                        }
                        writer.WriteLine("\t]");
                        writer.WriteLine("}");

                        if (currentGroup != 0)
                            unit_writer.WriteLine(",");

                        unit_writer.Write($"\t\t{{ \"$ref\": \"/elements/unit/{output_schema_version}/categories/unit-{name}.schema.json\" }}");
                        currentGroup++;
                    }
                }
                unit_writer.WriteLine();
                unit_writer.WriteLine("\t]");
                unit_writer.WriteLine("}");
            }
        }

        Console.WriteLine("Done");
    }
}

