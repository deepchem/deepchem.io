# deepchem.io
[![Build Status](https://travis-ci.org/deepchem/deepchem.io.svg?branch=master)](https://travis-ci.org/github/deepchem/deepchem.io)

Website for deepchem https://deepchem.io.


The static pages for the website are maintained in this repo.
Upon each pull request merged into master on this repo, a build
is triggered which pushes the static pages up to a bucket in S3
which is served.

The frontpage for the website is in `website/index.html`. The scripts which handle the push to S3 are in `devtools/`.

