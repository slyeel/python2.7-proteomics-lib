# Proteomics python library

This Python library, written for Python v2.7, provides classes and methods to
support Proteomics data interpretation. It is intended to be a library resource
for use by other software programmes rather than providing any distinct program
functionality. There are test modules to test the functionality of the code,
and these (as well as the Epydoc documentation) should provide an example for
implementation.

## Description

The Python library is separated into a number of different modules. These
modules are to separate different functionality. The modules available are:
  * Mascot

### Mascot module

Mascot is a piece of software produced by [Matrix
Science](http://www.matrixscience.com), and it's aim is to produce protein (via
peptide) identifications from raw spectral information from the mass
spectrometers. It is, in Europe, the accepted method for identifing the
proteins in a sample, particularly if the results are to be published.

The Mascot module currently provides the ability to examine Mascot search logs,
and the user and group configurations. To see the individual methods available,
and to see information regarding implementation of the code, see the Epydoc (a
code-generated documentation, similar to JavaDoc).

## Installation

*SEE [INSTALL](INSTALL)*

## Usage

*SEE [examples/README.md](examples/README.md)*

## Author(s)

Julian Selley <[j.selley@manchester.ac.uk](mailto:j.selley@manchester.ac.uk)>

## License

*SEE [LICENSE](LICENSE)*
