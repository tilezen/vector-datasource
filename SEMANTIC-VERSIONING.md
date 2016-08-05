#Semantic Versioning

When a new version of Tilezen is released, developers should be able to tell from the version increment how much effort it will take them to integrate the new tiles with their map. We use semantic versioning to communicate this.

###What is Semantic Versioning?

Semantic versioning (or [SemVer](http://semver.org/)) is a formalized way of making promises with an X.Y.Z version indicator.

#### Version components

- `MAJOR`.`MINOR`.`PATCH`, example: `1.0.0` (default)
- `MAJOR`.`MINOR`.`PATCH`-`POSTFIX`, example: `1.0.0-pre1` (optional)

#### Version parts:

1. **MAJOR** version **X** for incompatible API changes.
2. **MINOR** version **Y** when adding functionality in a backwards-compatible manner, and
3. **PATCH** version **Z** when fixing backwards-compatible bugs
4. **pre-release** version **-POSTFIX** when releasing developer previews

**NOTE:** The above applies _after_ software has reached as version `1.0.0`, no promises are made for earlier versions.

#### Developer level of effort:

- Major version X: **high** – significant integration challenges, read the changelog closely
- Minor version Y: **low** – some integration challenges, read the changelog
- Bug fixes Z: **none** – simply use the new tiles, ignore the changelog
- Pre-release POSTFIX: **low to high** – some to significant integration challenges, read the changelog

## Versioning the Tilezen API

Proposed that upon our `1.0.0` release Tilezen makes the following promises.

####MAJOR version increments:

1. **Remove** `common layer`
1. **Change** `common layer` **name**
1. **Remove** `common-optional layer`
1. **Change** `common-optional layer` **name**
1. **Remove** `common` feature **property** completely from all zooms
1. **Change** `common` feature **property name**
1. **Remove** `common-optional` feature **property** at zoom 14 or more
1. **Change** `common-optional` feature **property name**
1. **Remove** `optional` feature **property** at zoom 14 or more
1. **Change** `kind` **value name**
1. **Remove** `kind` **value** completely from all zooms
1. **Move** `kind` from one layer to another
1. **Additional merging** across `kind` **values** in zooms 14, 15, or 16 (or max zoom) by removing `common`, `common-optional`, and/or `optional` **properties** or other method
1. **Merging** within `kind` **values** at zooms 16 (or max zoom) by removing `common`, `common-optional`, and `optional` **properties** or other method
1. **Change** of >= -3 (earlier) to `min_zoom` or `max_zoom` to determine when `kind` is included
1. **Change** of >= +2 (later) to `min_zoom` or `max_zoom` to determine when `kind` is included

#### MINOR version increments:

1. **Add** `common` layer
1. **Add** `common-optional` layer
1. **Add** `common` feature **property**
1. **Add** `common-optional` feature **property**
1. **Add** `optional` feature **property**
1. **Add** new `kind` value
1. **Additional merging** across `kind` **values** at zooms 13 or less by removing `common`, `common-optional`, and `optional` **properties** or other method
1. **Additional merging** within `kind` **values** at zooms 13, 14, or 15 by removing `common`, `common-optional`, and `optional` **properties** or other method
1. **Reassign** 50% or more of existing `kind` **value** into a new `kind` **value**, when kind has 10,000 or more features
1. **Change** of >= -2 (earlier) to `min_zoom` or `max_zoom` **values** to determine when `kind` is included
1. **Change** of >= +1 (later) to `min_zoom` or `max_zoom` **values** to determine when `kind` is included
1. **Adjustments** to the overall map balance (proportion of features in one layer or another, proportion of `kind`s in a single layer)

#### PATCH version increments

1. **Add** `optional` layer
1. **Change** `optional` layer **name**
1. **Remove** `optional` layer
1. **Additional merging** within `kind` **values** at zooms 12 or less by removing `common`, `common-optional`, and `optional` **properties** or other method
1. **Reassign** less than 50% of existing `kind` **value** into a new `kind` value, when kind has 10,000 or more features
1. **Reassign** more than 50% of existing `kind` **value** into a new `kind` value, when kind has less than 10,000 features
1. **Change** of -1 to `min_zoom` or `max_zoom` **values** to determine when `kind` is included
1. **Add** unpublicised `kind`
1. **Remove** unpublicised `kind`
1. **Correct** a regression in the API (to the last good version)
1. **Correct** a newly added property name
1. **Correct** a newly added `kind` value

## Versioning Data

We do not version data features, but we do attempt to indicate the data source and the feature ID as assigned by that source so customers can investigate upstream changes.

### INDIVIDUAL FEATURES are not versioned

#### Examples:

1. **Addition** of new feature
1. **Complete removal** of feature
1. **Changes** to feature name
1. **Changes** to feature position &/or shape
1. **Changes** to feature property values (including removal if removed from original source)
1. **Changes** to feature `kind` (when upstream data source reclassifies them).
1. **Changes** to feature min_zoom &/or max_zoom when area or other signal changes upstream

### POLITICAL GEOGRAPHY is not versioned.

#### Examples:

1. Major additions, deletions to country names, borders, disputed territories, and capitals are possible and quality as a significant event. Generally the Natural Earth source we currently use for low zooms (0-8) doesn’t update frequently, but OpenStreetMap (used for zooms 9+), and Who’s On First (used for zooms 12+) are setup to update continuously. When possible, we aspire to advertise when a new version of Natural Earth is loaded into the database or a significant event occurs in another data source either via the Tilezen changelog or another channel.
1. Minor corrections to country names, borders, disputed territories, capitals, and other administrative geography are always possible and will not be tracked or advertised.

## Versioning the Service

#### MAJOR version increments:

1. Rollup of MAJOR Tilezen API changes
1. Remove a file format
1. Backwards incompatible change to a file format
1. Tilezen software dependency has a breaking change to the tile response

#### MINOR version increments:

1. Rollup of MINOR Tilezen API changes
1. Add a file format

#### PATCH version increments:

1. Rollup of PATCH Tilezen API changes
1. Backwards compatible change to a file format
1. Software dependency has a backwards compatible change or bug fix with no change to the tile response

## See also

- [VERSION](VERSION)
- http://semver.org
- https://github.com/nvkelso/natural-earth-vector/blob/master/README.md