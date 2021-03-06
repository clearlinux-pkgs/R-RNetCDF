#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RNetCDF
Version  : 2.4.2
Release  : 14
URL      : https://cran.r-project.org/src/contrib/RNetCDF_2.4-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RNetCDF_2.4-2.tar.gz
Summary  : Interface to 'NetCDF' Datasets
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-RNetCDF-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : netcdf-dev

%description
for efficient storage of array-oriented scientific data and descriptions.
  Most capabilities of 'NetCDF' version 4 are supported. Optional conversions
  of time units are enabled by 'UDUNITS' version 2, also from Unidata.

%package lib
Summary: lib components for the R-RNetCDF package.
Group: Libraries

%description lib
lib components for the R-RNetCDF package.


%prep
%setup -q -c -n RNetCDF
cd %{_builddir}/RNetCDF

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624483590

%install
export SOURCE_DATE_EPOCH=1624483590
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RNetCDF
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RNetCDF
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RNetCDF
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RNetCDF || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RNetCDF/DESCRIPTION
/usr/lib64/R/library/RNetCDF/INDEX
/usr/lib64/R/library/RNetCDF/LICENSE
/usr/lib64/R/library/RNetCDF/Meta/Rd.rds
/usr/lib64/R/library/RNetCDF/Meta/demo.rds
/usr/lib64/R/library/RNetCDF/Meta/features.rds
/usr/lib64/R/library/RNetCDF/Meta/hsearch.rds
/usr/lib64/R/library/RNetCDF/Meta/links.rds
/usr/lib64/R/library/RNetCDF/Meta/nsInfo.rds
/usr/lib64/R/library/RNetCDF/Meta/package.rds
/usr/lib64/R/library/RNetCDF/NAMESPACE
/usr/lib64/R/library/RNetCDF/NEWS
/usr/lib64/R/library/RNetCDF/R/RNetCDF
/usr/lib64/R/library/RNetCDF/R/RNetCDF.rdb
/usr/lib64/R/library/RNetCDF/R/RNetCDF.rdx
/usr/lib64/R/library/RNetCDF/demo/write1_readN.R
/usr/lib64/R/library/RNetCDF/demo/writeN_read1.R
/usr/lib64/R/library/RNetCDF/help/AnIndex
/usr/lib64/R/library/RNetCDF/help/RNetCDF.rdb
/usr/lib64/R/library/RNetCDF/help/RNetCDF.rdx
/usr/lib64/R/library/RNetCDF/help/aliases.rds
/usr/lib64/R/library/RNetCDF/help/paths.rds
/usr/lib64/R/library/RNetCDF/html/00Index.html
/usr/lib64/R/library/RNetCDF/html/R.css
/usr/lib64/R/library/RNetCDF/tests/RNetCDF-test.R
/usr/lib64/R/library/RNetCDF/udunits/udunits2.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RNetCDF/libs/RNetCDF.so
/usr/lib64/R/library/RNetCDF/libs/RNetCDF.so.avx2
/usr/lib64/R/library/RNetCDF/libs/RNetCDF.so.avx512
