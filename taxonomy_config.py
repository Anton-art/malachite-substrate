# =================================================================================
# ГЕНЕРАЛЬНАЯ КАРТА МАЛАХИТА (FULL PRODUCTION TAXONOMY)
# Версия: 5.2 (Syntropy Ready + Full Descriptions)
# =================================================================================


TAXONOMY = {
    # 1. НАУКА
    "01_SCIENCE": {
        "id": "DOM-SCI", "name": "Science", "type": "DOMAIN", "description": "Fundamental laws of nature and abstract knowledge.",
        "children": {
            "Axioms": {
                "id": "BR-AXIOMS", "name": "Fundamental Axioms", "type": "BRANCH", "description": "The primary directives of the Universe and Intelligence.",
                "children": {
                    "Universal_Laws": {"id": "GRP-UNIV_LAW", "name": "Universal Laws", "type": "GROUP", "description": "Meta-laws governing all systems (Syntropy, Entropy)."}
                }
            },
            "Formal_Sciences": {
                "id": "BR-FORMAL", "name": "Formal Sciences", "type": "BRANCH", "description": "Systems based on definitions and rules.",
                "children": {
                    "Algebra_Number": {"id": "GRP-MATH_ALG", "name": "Algebra & Number Theory", "type": "GROUP", "description": "Study of symbols and rules for manipulating them."},
                    "Geometry_Topology": {"id": "GRP-MATH_GEO", "name": "Geometry & Topology", "type": "GROUP", "description": "Properties of space, shape, and relative position."},
                    "Calculus_Analysis": {"id": "GRP-MATH_CALC", "name": "Calculus & Analysis", "type": "GROUP", "description": "Study of continuous change and limits."},
                    "Prob_Stats": {"id": "GRP-MATH_STAT", "name": "Probability & Statistics", "type": "GROUP", "description": "Analysis of random events and data."},
                    "Logic": {"id": "GRP-LOGIC", "name": "Logic Foundations", "type": "GROUP", "description": "Formal principles of reasoning."},
                    "Theoretical_CS": {"id": "GRP-CS_THEORY", "name": "Theoretical CS", "type": "GROUP", "description": "Mathematical foundations of computation."}
                }
            },
            "Physics": {
                "id": "BR-PHYS", "name": "Physics", "type": "BRANCH", "description": "Study of matter, energy, and forces.",
                "children": {
                    "Classical_Mech": {"id": "GRP-PHYS_MECH", "name": "Classical Mechanics", "type": "GROUP", "description": "Motion of macroscopic objects."},
                    "Thermodynamics": {"id": "GRP-PHYS_THERM", "name": "Thermodynamics", "type": "GROUP", "description": "Heat, work, and entropy."},
                    "Electromagnetism": {"id": "GRP-PHYS_EM", "name": "Electromagnetism", "type": "GROUP", "description": "Electric and magnetic fields."},
                    "Quantum_Relativity": {"id": "GRP-PHYS_QUANT", "name": "Quantum & Relativity", "type": "GROUP", "description": "Physics of the very small and very fast."},
                    "Fluid_Dynamics": {"id": "GRP-PHYS_FLUID", "name": "Fluid Dynamics", "type": "GROUP", "description": "Flow of liquids and gases."}
                }
            },
            "Phenomena": {
                "id": "BR-PHEN", "name": "Phenomena & Effects", "type": "BRANCH", "description": "Observable physical effects used in engineering.",
                "children": {
                    "Optical_Effects": {"id": "GRP-EFF_OPT", "name": "Optical Effects", "type": "GROUP", "description": "Interaction of light with matter (Refraction, Diffraction)."},
                    "Electrical_Effects": {"id": "GRP-EFF_ELEC", "name": "Electrical Effects", "type": "GROUP", "description": " piezoelectricity, thermoelectricity, etc."},
                    "Quantum_Effects": {"id": "GRP-EFF_QUANT", "name": "Quantum Effects", "type": "GROUP", "description": "Tunneling, Entanglement, Superconductivity."},
                    "Chemical_Reactions": {"id": "GRP-EFF_CHEM", "name": "Named Reactions", "type": "GROUP", "description": "Specific chemical transformations (Haber-Bosch, etc)."}
                }
            },
            "Chemistry": {
                "id": "BR-CHEM", "name": "Chemistry", "type": "BRANCH", "description": "Study of substances and their changes.",
                "children": {
                    "Inorganic": {"id": "GRP-CHEM_INORG", "name": "Inorganic Chemistry", "type": "GROUP", "description": "Properties of non-carbon compounds."},
                    "Organic": {"id": "GRP-CHEM_ORG", "name": "Organic Chemistry", "type": "GROUP", "description": "Structure and reactions of carbon compounds."},
                    "Physical_Chem": {"id": "GRP-CHEM_PHYS", "name": "Physical Chemistry", "type": "GROUP", "description": "Physics of chemical systems (Kinetics, Thermo)."},
                    "Analytical": {"id": "GRP-CHEM_ANAL", "name": "Analytical Chemistry", "type": "GROUP", "description": "Methods for identifying matter."}
                }
            },
            "Biology": {
                "id": "BR-BIO", "name": "Biology", "type": "BRANCH", "description": "Study of life.",
                "children": {
                    "Genetics": {"id": "GRP-BIO_GEN", "name": "Genetics & Molecular", "type": "GROUP", "description": "Heredity and DNA."},
                    "Cell_Biology": {"id": "GRP-BIO_CELL", "name": "Cell Biology", "type": "GROUP", "description": "Structure and function of the cell."},
                    "Physiology": {"id": "GRP-BIO_PHYS", "name": "Physiology & Anatomy", "type": "GROUP", "description": "Functions of living organisms."},
                    "Evolution": {"id": "GRP-BIO_EVO", "name": "Evolution & Ecology", "type": "GROUP", "description": "Origin of species and ecosystems."},
                    "Microbiology": {"id": "GRP-BIO_MICRO", "name": "Microbiology & Virology", "type": "GROUP", "description": "Study of microscopic organisms."}
                }
            },
            "Geoscience": {
                "id": "BR-GEO", "name": "Geoscience", "type": "BRANCH", "description": "Study of Earth and Space.",
                "children": {
                    "Geology": {"id": "GRP-GEO_TECT", "name": "Geology & Tectonics", "type": "GROUP", "description": "Solid Earth structure and history."},
                    "Atmospheric": {"id": "GRP-GEO_ATM", "name": "Atmospheric Science", "type": "GROUP", "description": "Weather and climate."},
                    "Oceanography": {"id": "GRP-GEO_OCEAN", "name": "Oceanography", "type": "GROUP", "description": "The ocean ecosystem."},
                    "Astronomy": {"id": "GRP-ASTRO", "name": "Astronomy & Cosmology", "type": "GROUP", "description": "Celestial bodies and the Universe."}
                }
            },
            "Reference_Data": {
                "id": "BR-DATA", "name": "Reference Data", "type": "BRANCH", "description": "Constants and links to raw data.",
                "children": {
                    "Constants": {"id": "GRP-CONST", "name": "Physical Constants", "type": "GROUP", "description": "Universal constants (c, G, h)."},
                    "Datasets": {"id": "GRP-DATA", "name": "Datasets Metadata", "type": "GROUP", "description": "Links to external large datasets."}
                }
            }
        }
    },


    # 2. ПРОЕКТИРОВАНИЕ
    "02_DESIGN": {
        "id": "DOM-DES", "name": "Design", "type": "DOMAIN", "description": "Information templates, standards, and code.",
        "children": {
            "Standards_General": {
                "id": "BR-STD_GEN", "name": "General Standards", "type": "BRANCH", "description": "Universal engineering standards.",
                "children": {
                    "Metrology": {"id": "GRP-STD_METRO", "name": "Metrology & Units", "type": "GROUP", "description": "SI units and measurement standards."},
                    "Drawing": {"id": "GRP-STD_DRAW", "name": "Technical Drawing", "type": "GROUP", "description": "GD&T and drafting rules."},
                    "Quality": {"id": "GRP-STD_QUAL", "name": "Quality Management", "type": "GROUP", "description": "ISO 9000 and QA methodologies."}
                }
            },
            "Standards_Mechanical": {
                "id": "BR-STD_MECH", "name": "Mechanical Standards", "type": "BRANCH", "description": "Standards for physical machinery.",
                "children": {
                    "Fasteners": {"id": "GRP-STD_FAST", "name": "Fasteners & Hardware", "type": "GROUP", "description": "Threads, bolts, screws standards."},
                    "Materials_Test": {"id": "GRP-STD_MAT", "name": "Materials Testing", "type": "GROUP", "description": "ASTM/ISO testing protocols."},
                    "Pressure": {"id": "GRP-STD_PRESS", "name": "Pressure Vessels", "type": "GROUP", "description": "ASME Boiler codes."},
                    "Gears": {"id": "GRP-STD_GEAR", "name": "Gears & Bearings", "type": "GROUP", "description": "AGMA/ISO gear standards."}
                }
            },
            "Standards_Electrical": {
                "id": "BR-STD_ELEC", "name": "Electrical Standards", "type": "BRANCH", "description": "Standards for electronics and power.",
                "children": {
                    "Safety": {"id": "GRP-STD_SAFE", "name": "Electrical Safety", "type": "GROUP", "description": "IEC/UL safety codes."},
                    "PCB": {"id": "GRP-STD_PCB", "name": "Electronics & PCB", "type": "GROUP", "description": "IPC standards for circuit boards."},
                    "Motors": {"id": "GRP-STD_MOTOR", "name": "Motors & Generators", "type": "GROUP", "description": "NEMA/IEC motor standards."}
                }
            },
            "Standards_Digital": {
                "id": "BR-STD_DIG", "name": "Digital Standards", "type": "BRANCH", "description": "Protocols and formats.",
                "children": {
                    "Protocols": {"id": "GRP-STD_NET", "name": "Networking Protocols", "type": "GROUP", "description": "TCP/IP, HTTP, Bluetooth."},
                    "Wireless": {"id": "GRP-STD_WIFI", "name": "Wireless Standards", "type": "GROUP", "description": "IEEE 802.11, 5G."},
                    "Formats": {"id": "GRP-STD_FMT", "name": "Data Formats", "type": "GROUP", "description": "JSON, XML, CSV specs."},
                    "Security": {"id": "GRP-STD_SEC", "name": "Cybersecurity", "type": "GROUP", "description": "NIST, ISO 27001."}
                }
            },
            "Methodologies": {
                "id": "BR-METH", "name": "Methodologies", "type": "BRANCH", "description": "Ways of working and thinking.",
                "children": {
                    "TRIZ": {"id": "GRP-METH_TRIZ", "name": "TRIZ & Systems Eng", "type": "GROUP", "description": "Theory of Inventive Problem Solving."},
                    "Agile": {"id": "GRP-METH_AGILE", "name": "Agile & DevOps", "type": "GROUP", "description": "Iterative development methods."},
                    "Lean": {"id": "GRP-METH_LEAN", "name": "Lean & Project Mgmt", "type": "GROUP", "description": "Waste reduction and efficiency."}
                }
            },
            "Software_Source": {
                "id": "BR-CODE", "name": "Software Source", "type": "BRANCH", "description": "Code that powers the system.",
                "children": {
                    "Languages": {"id": "GRP-LANG", "name": "Programming Languages", "type": "GROUP", "description": "Python, C++, Rust specs."},
                    "Algorithms": {"id": "GRP-ALGO", "name": "Algorithms Library", "type": "GROUP", "description": "Sorting, Search, AI algorithms."},
                    "Patterns": {"id": "GRP-PAT", "name": "Design Patterns", "type": "GROUP", "description": "Singleton, Factory, Observer."},
                    "Architectures": {"id": "GRP-ARCH", "name": "System Architectures", "type": "GROUP", "description": "Microservices, Monolith, Serverless."}
                }
            }
        }
    },


    # 3. РЕСУРСЫ
    "03_RESOURCES": {
        "id": "DOM-RES", "name": "Resources", "type": "DOMAIN", "description": "Raw materials from the planet.",
        "children": {
            "Minerals": {
                "id": "BR-MIN", "name": "Minerals", "type": "BRANCH", "description": "Solid inorganic resources.",
                "children": {
                    "Ferrous": {"id": "GRP-ORE_FE", "name": "Ferrous Ores", "type": "GROUP", "description": "Iron, Manganese, Chrome ores."},
                    "Base_Metals": {"id": "GRP-ORE_BASE", "name": "Base Metals Ores", "type": "GROUP", "description": "Copper, Zinc, Lead, Nickel ores."},
                    "Precious": {"id": "GRP-ORE_PREC", "name": "Precious Ores", "type": "GROUP", "description": "Gold, Silver, Platinum ores."},
                    "Tech_Critical": {"id": "GRP-ORE_TECH", "name": "Tech Critical Minerals", "type": "GROUP", "description": "Lithium, Cobalt, Rare Earths."},
                    "Construction": {"id": "GRP-MIN_CONST", "name": "Construction Aggregates", "type": "GROUP", "description": "Sand, Gravel, Limestone."},
                    "Chemical": {"id": "GRP-MIN_CHEM", "name": "Chemical Minerals", "type": "GROUP", "description": "Salt, Potash, Sulfur."},
                    "Gemstones": {"id": "GRP-GEMS", "name": "Gemstones", "type": "GROUP", "description": "Diamonds, Rubies, Sapphires."}
                }
            },
            "Hydrocarbons": {
                "id": "BR-HYDRO", "name": "Hydrocarbons", "type": "BRANCH", "description": "Fossil fuels.",
                "children": {
                    "Crude_Oil": {"id": "GRP-OIL", "name": "Crude Oil", "type": "GROUP", "description": "Liquid petroleum."},
                    "Natural_Gas": {"id": "GRP-GAS", "name": "Natural Gas", "type": "GROUP", "description": "Methane and associated gases."},
                    "NGL": {"id": "GRP-NGL", "name": "NGL & Condensates", "type": "GROUP", "description": "Ethane, Propane, Butane."},
                    "Coal": {"id": "GRP-COAL", "name": "Coal & Solid Fuels", "type": "GROUP", "description": "Anthracite, Lignite, Peat."}
                }
            },
            "Biosphere": {
                "id": "BR-BIO", "name": "Biosphere", "type": "BRANCH", "description": "Renewable biological resources.",
                "children": {
                    "Timber": {"id": "GRP-TIMBER", "name": "Forestry & Timber", "type": "GROUP", "description": "Wood and forest products."},
                    "Cereals": {"id": "GRP-CROP_CER", "name": "Cereal Crops", "type": "GROUP", "description": "Wheat, Rice, Corn."},
                    "Oils_Fibers": {"id": "GRP-CROP_IND", "name": "Oil & Fiber Crops", "type": "GROUP", "description": "Cotton, Soy, Palm Oil."},
                    "Livestock": {"id": "GRP-LIVESTOCK", "name": "Livestock", "type": "GROUP", "description": "Cattle, Poultry, Swine."},
                    "Fisheries": {"id": "GRP-FISH", "name": "Fisheries", "type": "GROUP", "description": "Wild catch and aquaculture."}
                }
            },
            "Environment": {
                "id": "BR-ENV", "name": "Environment", "type": "BRANCH", "description": "Global commons.",
                "children": {
                    "Water": {"id": "GRP-WATER", "name": "Water Resources", "type": "GROUP", "description": "Fresh and Saline water."},
                    "Air": {"id": "GRP-AIR", "name": "Atmospheric Gases", "type": "GROUP", "description": "Nitrogen, Oxygen, Argon."},
                    "Energy_Flows": {"id": "GRP-NRG_FLOW", "name": "Solar & Wind Flows", "type": "GROUP", "description": "Renewable energy potential."},
                    "Space": {"id": "GRP-SPACE", "name": "Land & Spectrum", "type": "GROUP", "description": "Territory and Radio Spectrum."}
                }
            }
        }
    },


    # 4. МАТЕРИАЛЫ
    "04_MATERIALS": {
        "id": "DOM-MAT", "name": "Materials", "type": "DOMAIN", "description": "Processed substances with defined properties.",
        "children": {
            "Metals_Ferrous": {
                "id": "BR-MET_FE", "name": "Ferrous Metals", "type": "BRANCH", "description": "Iron-based alloys.",
                "children": {
                    "Carbon_Steels": {"id": "GRP-STL_C", "name": "Carbon Steels", "type": "GROUP", "description": "Standard steels (Low/Med/High Carbon)."},
                    "Alloy_Steels": {"id": "GRP-STL_A", "name": "Alloy Steels", "type": "GROUP", "description": "Steels with other elements (Cr, Mo, V)."},
                    "Stainless": {"id": "GRP-STL_S", "name": "Stainless Steels", "type": "GROUP", "description": "Corrosion resistant steels."},
                    "Tool_Steels": {"id": "GRP-STL_T", "name": "Tool Steels", "type": "GROUP", "description": "Hard steels for cutting and forming."},
                    "Cast_Irons": {"id": "GRP-IRON", "name": "Cast Irons", "type": "GROUP", "description": "High carbon iron alloys."}
                }
            },
            "Metals_NonFerrous": {
                "id": "BR-MET_NF", "name": "Non-Ferrous Metals", "type": "BRANCH", "description": "Metals without iron.",
                "children": {
                    "Aluminum": {"id": "GRP-AL", "name": "Aluminum Alloys", "type": "GROUP", "description": "Lightweight alloys."},
                    "Copper": {"id": "GRP-CU", "name": "Copper Alloys", "type": "GROUP", "description": "Conductive alloys (Brass, Bronze)."},
                    "Titanium": {"id": "GRP-TI", "name": "Titanium Alloys", "type": "GROUP", "description": "High strength-to-weight ratio."},
                    "Magnesium": {"id": "GRP-MG", "name": "Magnesium Alloys", "type": "GROUP", "description": "Ultra-light alloys."},
                    "Superalloys": {"id": "GRP-SUPER", "name": "Nickel Superalloys", "type": "GROUP", "description": "High-temperature alloys for turbines."},
                    "Precious": {"id": "GRP-PREC", "name": "Precious Metals", "type": "GROUP", "description": "Gold, Silver, Platinum."}
                }
            },
            "Polymers": {
                "id": "BR-POLY", "name": "Polymers", "type": "BRANCH", "description": "Plastics and rubbers.",
                "children": {
                    "Commodity_TP": {"id": "GRP-TP_COM", "name": "Commodity Thermoplastics", "type": "GROUP", "description": "PE, PP, PVC, PET."},
                    "Engineering_TP": {"id": "GRP-TP_ENG", "name": "Engineering Plastics", "type": "GROUP", "description": "Nylon, ABS, PC."},
                    "Thermosets": {"id": "GRP-TS", "name": "Thermosets", "type": "GROUP", "description": "Epoxy, Phenolic, Polyurethane."},
                    "Elastomers": {"id": "GRP-EL", "name": "Elastomers & Rubbers", "type": "GROUP", "description": "Natural and Synthetic Rubber, Silicone."}
                }
            },
            "Chemicals": {
                "id": "BR-CHEM", "name": "Chemicals", "type": "BRANCH", "description": "Industrial chemicals.",
                "children": {
                    "Gases": {"id": "GRP-GAS", "name": "Industrial Gases", "type": "GROUP", "description": "Processed gases (Liquid O2, N2)."},
                    "Acids_Bases": {"id": "GRP-ACID", "name": "Acids & Bases", "type": "GROUP", "description": "Sulfuric acid, Caustic soda."},
                    "Solvents": {"id": "GRP-SOLV", "name": "Solvents", "type": "GROUP", "description": "Alcohols, Acetone."},
                    "Salts": {"id": "GRP-SALT", "name": "Salts", "type": "GROUP", "description": "Chlorides, Sulfates, Nitrates."},
                    "Catalysts": {"id": "GRP-CAT", "name": "Catalysts", "type": "GROUP", "description": "Substances that speed up reactions."}
                }
            },
            "Ceramics": {
                "id": "BR-CERAM", "name": "Ceramics", "type": "BRANCH", "description": "Inorganic non-metallic solids.",
                "children": {
                    "Glass": {"id": "GRP-GLASS", "name": "Glass", "type": "GROUP", "description": "Float glass, Borosilicate."},
                    "Tech_Ceramics": {"id": "GRP-CER_TECH", "name": "Technical Ceramics", "type": "GROUP", "description": "Alumina, Zirconia, Carbides."},
                    "Construction": {"id": "GRP-CER_CONST", "name": "Construction Ceramics", "type": "GROUP", "description": "Brick, Cement, Concrete."},
                    "Composites": {"id": "GRP-COMP", "name": "Composites", "type": "GROUP", "description": "Fiberglass, Carbon Fiber."}
                }
            }
        }
    },


    # 5. ИНФРАСТРУКТУРА
    "05_INFRASTRUCTURE": {
        "id": "DOM-INFRA", "name": "Infrastructure", "type": "DOMAIN", "description": "Means of production and facilities.",
        "children": {
            "Facilities": {
                "id": "BR-FAC", "name": "Facilities", "type": "BRANCH", "description": "Buildings and complexes.",
                "children": {
                    "Heavy_Ind": {"id": "GRP-FAC_HEAVY", "name": "Heavy Industry Plants", "type": "GROUP", "description": "Steel mills, Refineries."},
                    "Light_Ind": {"id": "GRP-FAC_LIGHT", "name": "Light Industry Factories", "type": "GROUP", "description": "Assembly plants, Textile mills."},
                    "High_Tech": {"id": "GRP-FAC_TECH", "name": "High Tech Fabs", "type": "GROUP", "description": "Semiconductor fabs, Clean rooms."},
                    "Energy": {"id": "GRP-FAC_NRG", "name": "Power Stations", "type": "GROUP", "description": "Power plants (Nuclear, Solar, Coal)."},
                    "Logistics": {"id": "GRP-FAC_LOG", "name": "Logistics & Ports", "type": "GROUP", "description": "Warehouses, Ports, Airports."}
                }
            },
            "Machines": {
                "id": "BR-MACH", "name": "Machines", "type": "BRANCH", "description": "Active machinery.",
                "children": {
                    "CNC": {"id": "GRP-MACH_CNC", "name": "CNC Machining Centers", "type": "GROUP", "description": "Mills, Lathes."},
                    "Grinding": {"id": "GRP-MACH_GRIND", "name": "Grinding & Finishing", "type": "GROUP", "description": "Surface grinders, Polishers."},
                    "Cutting": {"id": "GRP-MACH_CUT", "name": "Cutting", "type": "GROUP", "description": "Laser, Plasma, Waterjet."},
                    "Forming": {"id": "GRP-MACH_FORM", "name": "Presses & Molding", "type": "GROUP", "description": "Hydraulic presses, Injection molding."},
                    "Additive": {"id": "GRP-MACH_ADD", "name": "Industrial 3D Printers", "type": "GROUP", "description": "FDM, SLA, SLS printers."},
                    "Robotics": {"id": "GRP-MACH_BOT", "name": "Industrial Robots", "type": "GROUP", "description": "Arms, AGVs."}
                }
            },
            "Tools": {
                "id": "BR-TOOL", "name": "Tools", "type": "BRANCH", "description": "Passive tools and consumables.",
                "children": {
                    "Cutting_Tools": {"id": "GRP-TOOL_CUT", "name": "Cutting Tools", "type": "GROUP", "description": "Drills, Endmills, Inserts."},
                    "Molds": {"id": "GRP-TOOL_MOLD", "name": "Molds & Dies", "type": "GROUP", "description": "Tooling for casting and molding."},
                    "Metrology": {"id": "GRP-TOOL_MEAS", "name": "Metrology", "type": "GROUP", "description": "Calipers, CMMs, Gauges."},
                    "Hand_Tools": {"id": "GRP-TOOL_HAND", "name": "Hand & Power Tools", "type": "GROUP", "description": "Wrenches, Drills, Hammers."}
                }
            }
        }
    },


    # 6. ПРОЦЕССЫ
    "06_PROCESSES": {
        "id": "DOM-PROC", "name": "Processes", "type": "DOMAIN", "description": "Technological actions.",
        "children": {
            "Manufacturing": {
                "id": "BR-MFG", "name": "Manufacturing", "type": "BRANCH", "description": "Making things.",
                "children": {
                    "Casting": {"id": "GRP-PROC_CAST", "name": "Casting", "type": "GROUP", "description": "Pouring liquid into a mold."},
                    "Molding": {"id": "GRP-PROC_MOLD", "name": "Molding", "type": "GROUP", "description": "Shaping plastic/rubber."},
                    "Deformation": {"id": "GRP-PROC_DEF", "name": "Deformation", "type": "GROUP", "description": "Forging, Rolling, Extrusion."},
                    "Machining": {"id": "GRP-PROC_MACH", "name": "Machining", "type": "GROUP", "description": "Removing material (Turning, Milling)."},
                    "Welding": {"id": "GRP-PROC_WELD", "name": "Welding & Joining", "type": "GROUP", "description": "Fusing materials together."},
                    "Additive": {"id": "GRP-PROC_ADD", "name": "Additive Processes", "type": "GROUP", "description": "Building layer by layer."},
                    "Heat_Treat": {"id": "GRP-PROC_HEAT", "name": "Heat Treatment", "type": "GROUP", "description": "Hardening, Annealing."},
                    "Finishing": {"id": "GRP-PROC_FIN", "name": "Surface Finishing", "type": "GROUP", "description": "Painting, Plating, Polishing."}
                }
            },
            "Synthesis": {
                "id": "BR-SYNTH", "name": "Synthesis", "type": "BRANCH", "description": "Creating materials.",
                "children": {
                    "Metallurgy": {"id": "GRP-PROC_METAL", "name": "Metallurgy", "type": "GROUP", "description": "Smelting and refining metals."},
                    "Chemical": {"id": "GRP-PROC_CHEM", "name": "Chemical Synthesis", "type": "GROUP", "description": "Creating chemicals."},
                    "Biotech": {"id": "GRP-PROC_BIO", "name": "Biotech Processes", "type": "GROUP", "description": "Fermentation, Genetic engineering."}
                }
            },
            "Logistics": {
                "id": "BR-LOG", "name": "Logistics", "type": "BRANCH", "description": "Moving and maintaining.",
                "children": {
                    "Transport": {"id": "GRP-PROC_TRANS", "name": "Transport", "type": "GROUP", "description": "Shipping, Rail, Air freight."},
                    "Maintenance": {"id": "GRP-PROC_MAINT", "name": "Maintenance", "type": "GROUP", "description": "Repair and upkeep."}
                }
            }
        }
    },


    # 7. АРТЕФАКТЫ
    "07_ARTIFACTS": {
        "id": "DOM-ART", "name": "Artifacts", "type": "DOMAIN", "description": "Man-made objects.",
        "children": {
            "Parts_Mechanical": {
                "id": "BR-PART_MECH", "name": "Mechanical Parts", "type": "BRANCH", "description": "Simple mechanical components.",
                "children": {
                    "Fasteners": {"id": "GRP-FASTEN", "name": "Fasteners", "type": "GROUP", "description": "Bolts, Nuts, Screws."},
                    "Bearings": {"id": "GRP-BEAR", "name": "Bearings", "type": "GROUP", "description": "Ball, Roller, Plain bearings."},
                    "Seals": {"id": "GRP-SEAL", "name": "Seals & Gaskets", "type": "GROUP", "description": "O-rings, Gaskets."},
                    "Springs": {"id": "GRP-SPRING", "name": "Springs", "type": "GROUP", "description": "Coil, Leaf springs."},
                    "Gears": {"id": "GRP-GEAR", "name": "Gears", "type": "GROUP", "description": "Spur, Helical, Bevel gears."},
                    "Pipes": {"id": "GRP-PIPE", "name": "Pipes & Fittings", "type": "GROUP", "description": "Tubes, Valves, Flanges."}
                }
            },
            "Parts_Electronic": {
                "id": "BR-PART_ELEC", "name": "Electronic Parts", "type": "BRANCH", "description": "Discrete electronic components.",
                "children": {
                    "Resistors": {"id": "GRP-RES", "name": "Resistors", "type": "GROUP", "description": "Fixed and variable resistors."},
                    "Capacitors": {"id": "GRP-CAP", "name": "Capacitors", "type": "GROUP", "description": "Ceramic, Electrolytic capacitors."},
                    "Inductors": {"id": "GRP-IND", "name": "Inductors", "type": "GROUP", "description": "Coils, Transformers."},
                    "Diodes": {"id": "GRP-DIODE", "name": "Diodes", "type": "GROUP", "description": "Rectifiers, LEDs."},
                    "Transistors": {"id": "GRP-TRANS", "name": "Transistors", "type": "GROUP", "description": "BJT, MOSFETs."},
                    "Connectors": {"id": "GRP-CONN", "name": "Connectors", "type": "GROUP", "description": "Plugs, Sockets."},
                    "Sensors": {"id": "GRP-SENS", "name": "Sensors", "type": "GROUP", "description": "Temp, Pressure, Light sensors."}
                }
            },
            "Parts_Chips": {
                "id": "BR-PART_IC", "name": "Integrated Circuits", "type": "BRANCH", "description": "Complex chips.",
                "children": {
                    "Logic": {"id": "GRP-IC_LOGIC", "name": "Logic ICs", "type": "GROUP", "description": "Gates, Flip-flops."},
                    "MCU": {"id": "GRP-IC_MCU", "name": "Microcontrollers", "type": "GROUP", "description": "CPUs, MCUs."},
                    "Memory": {"id": "GRP-IC_MEM", "name": "Memory", "type": "GROUP", "description": "RAM, ROM, Flash."},
                    "Power_IC": {"id": "GRP-IC_PWR", "name": "Power Management", "type": "GROUP", "description": "Regulators, Converters."}
                }
            },
            "Assemblies": {
                "id": "BR-ASM", "name": "Assemblies", "type": "BRANCH", "description": "Functional units.",
                "children": {
                    "Engines": {"id": "GRP-ASM_ENG", "name": "Engines (ICE)", "type": "GROUP", "description": "Internal Combustion Engines."},
                    "Motors": {"id": "GRP-ASM_MOT", "name": "Electric Motors", "type": "GROUP", "description": "AC/DC Motors."},
                    "Batteries": {"id": "GRP-ASM_BATT", "name": "Batteries", "type": "GROUP", "description": "Battery packs."},
                    "Transmissions": {"id": "GRP-ASM_TRANS", "name": "Transmissions", "type": "GROUP", "description": "Gearboxes."},
                    "PCBs": {"id": "GRP-ASM_PCB", "name": "PCB Modules", "type": "GROUP", "description": "Assembled circuit boards."},
                    "Displays": {"id": "GRP-ASM_DISP", "name": "Displays", "type": "GROUP", "description": "LCD, OLED screens."},
                    "Chassis": {"id": "GRP-ASM_CHAS", "name": "Chassis & Frames", "type": "GROUP", "description": "Structural frames."}
                }
            },
            "Products_Mobility": {
                "id": "BR-PROD_MOB", "name": "Mobility Products", "type": "BRANCH", "description": "Vehicles.",
                "children": {
                    "Cars": {"id": "GRP-VEH_CAR", "name": "Cars & Light Trucks", "type": "GROUP", "description": "Passenger vehicles."},
                    "Trucks": {"id": "GRP-VEH_TRUCK", "name": "Heavy Trucks & Buses", "type": "GROUP", "description": "Commercial transport."},
                    "Bikes": {"id": "GRP-VEH_BIKE", "name": "Motorcycles", "type": "GROUP", "description": "Two-wheelers."},
                    "Aircraft": {"id": "GRP-VEH_AIR", "name": "Aircraft", "type": "GROUP", "description": "Planes, Helicopters, Drones."},
                    "Ships": {"id": "GRP-VEH_SHIP", "name": "Ships & Boats", "type": "GROUP", "description": "Marine vessels."},
                    "Trains": {"id": "GRP-VEH_TRAIN", "name": "Trains", "type": "GROUP", "description": "Locomotives and wagons."},
                    "Space": {"id": "GRP-VEH_SPACE", "name": "Spacecraft", "type": "GROUP", "description": "Rockets, Satellites."}
                }
            },
            "Products_Consumer": {
                "id": "BR-PROD_CONS", "name": "Consumer Products", "type": "BRANCH", "description": "Goods for people.",
                "children": {
                    "Computers": {"id": "GRP-CONS_PC", "name": "Computers", "type": "GROUP", "description": "Laptops, Desktops."},
                    "Phones": {"id": "GRP-CONS_PHONE", "name": "Smartphones", "type": "GROUP", "description": "Mobile phones."},
                    "Wearables": {"id": "GRP-CONS_WEAR", "name": "Wearables", "type": "GROUP", "description": "Watches, Trackers."},
                    "Appliances": {"id": "GRP-CONS_APP", "name": "Home Appliances", "type": "GROUP", "description": "Fridges, Washing machines."}
                }
            },
            "Products_Industrial": {
                "id": "BR-PROD_IND", "name": "Industrial Products", "type": "BRANCH", "description": "Goods for industry.",
                "children": {
                    "Construction": {"id": "GRP-IND_CONST", "name": "Construction Machinery", "type": "GROUP", "description": "Excavators, Cranes."},
                    "Agri": {"id": "GRP-IND_AGRI", "name": "Agricultural Machinery", "type": "GROUP", "description": "Tractors, Harvesters."},
                    "Medical": {"id": "GRP-IND_MED", "name": "Medical Devices", "type": "GROUP", "description": "MRI, Ventilators."},
                    "Defense": {"id": "GRP-IND_DEF", "name": "Defense Systems", "type": "GROUP", "description": "Weapons, Radar."}
                }
            },
            "Structures": {
                "id": "BR-STRUCT", "name": "Structures", "type": "BRANCH", "description": "Immovable objects.",
                "children": {
                    "Residential": {"id": "GRP-STR_RES", "name": "Residential Buildings", "type": "GROUP", "description": "Houses, Apartments."},
                    "Commercial": {"id": "GRP-STR_COM", "name": "Commercial Buildings", "type": "GROUP", "description": "Offices, Malls."},
                    "Industrial": {"id": "GRP-STR_IND", "name": "Industrial Facilities", "type": "GROUP", "description": "Factories, Warehouses."},
                    "Infrastructure": {"id": "GRP-STR_INF", "name": "Civil Infrastructure", "type": "GROUP", "description": "Bridges, Roads, Dams."}
                }
            }
        }
    },


    # 8. ОБЩЕСТВО
    "08_SOCIETY": {
        "id": "DOM-SOC", "name": "Society", "type": "DOMAIN", "description": "Context, Needs, and Rules.",
        "children": {
            "History": {
                "id": "BR-HIST", "name": "History", "type": "BRANCH", "description": "The timeline of events.",
                "children": {
                    "Events": {"id": "GRP-HIST_EVENT", "name": "Historical Events", "type": "GROUP", "description": "Wars, Discoveries, Treaties."},
                    "Eras": {"id": "GRP-HIST_ERA", "name": "Eras & Periods", "type": "GROUP", "description": "Time periods."}
                }
            },
            "Economics": {
                "id": "BR-ECON", "name": "Economics", "type": "BRANCH", "description": "Production and consumption.",
                "children": {
                    "Markets": {"id": "GRP-ECON_MKT", "name": "Markets & Commodities", "type": "GROUP", "description": "Stock markets, Resource prices."},
                    "Companies": {"id": "GRP-ECON_CORP", "name": "Companies", "type": "GROUP", "description": "Corporations and entities."},
                    "Indicators": {"id": "GRP-ECON_IND", "name": "Economic Indicators", "type": "GROUP", "description": "GDP, Inflation."},
                    "Trade": {"id": "GRP-ECON_TRADE", "name": "Trade & Logistics", "type": "GROUP", "description": "Trade routes and agreements."}
                }
            },
            "Humanity": {
                "id": "BR-HUM", "name": "Humanity", "type": "BRANCH", "description": "The human factor.",
                "children": {
                    "Needs": {"id": "GRP-HUM_NEED", "name": "Human Needs", "type": "GROUP", "description": "Maslow's hierarchy."},
                    "Legal": {"id": "GRP-HUM_LAW", "name": "Legal Frameworks", "type": "GROUP", "description": "Laws and regulations."},
                    "Geopolitics": {"id": "GRP-HUM_GEO", "name": "Geopolitics", "type": "GROUP", "description": "Countries and borders."},
                    "Ethics": {"id": "GRP-HUM_ETH", "name": "Ethics & Risks", "type": "GROUP", "description": "Moral dilemmas and existential risks."}
                }
            }
        }
    }
}