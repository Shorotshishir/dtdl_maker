from Data.Turbine import Turbine
from core import serialize_to_dtdl

# Create an instance of the Turbine class

if __name__ == '__main__':
    turbine = Turbine("1", False)

    # Generate DTDL
    dtdl = serialize_to_dtdl(turbine,
                             1,
                             "Wind Turbine",
                             "Wind Turbine data")
    print(turbine.__class__.__name__)
    with open(f"{turbine.__class__.__name__}.json", "w+") as f:
        f.write(dtdl)

