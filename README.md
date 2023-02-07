# Arista License File renamer

Small script to rename license files provided to expose customer and serial number for easier management in projects.


## Setup

```bash
pip install git+https://github.com/titom73/arista-license-rename.git
```

## Usage

```bash
$ ar-lic-cleaner rename --help
Usage: ar-lic-cleaner rename [OPTIONS]

Options:
  -i, --input PATH        Path where license files are located
  --backup / --no-backup  Save original lic under input/backup
  --help                  Show this message and exit.
```

## Example

```bash
$ ar-lic-cleaner rename --input data --backup
Start reading folder data for license file
- License file: license_MACsec_13.json renamed to CUSTOMER01-JPxxxxxxxx-lic.json
- License file: license_MACsec_2.json renamed to  CUSTOMER01-JPxxxxxxxx-lic.json
```

## License

Code is under Apache2 License
