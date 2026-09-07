# Palmerston North City Council

Support for rubbish and recycling schedules provided by [Palmerston North City Council](https://www.pncc.govt.nz/Services/Rubbish-and-recycling/Palmy-Collections/Rubbish-and-recycling-days).

## Configuration via configuration.yaml

```yaml
waste_collection_schedule:
  sources:
    - name: pncc_govt_nz
      args:
        address: ADDRESS
```

### Configuration Variables

**address**  
*(string) (required)*

The full property address returned by the council's address search.

## How to get the source arguments

Visit the [Palmerston North City Council rubbish and recycling days page](https://www.pncc.govt.nz/Services/Rubbish-and-recycling/Palmy-Collections/Rubbish-and-recycling-days), search for your property, and use the full address shown in the search results.
