#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-RNetCDF
Version  : 2.8.1
Release  : 32
URL      : https://cran.r-project.org/src/contrib/RNetCDF_2.8-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RNetCDF_2.8-1.tar.gz
Summary  : Interface to 'NetCDF' Datasets
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+
Requires: R-RNetCDF-lib = %{version}-%{release}
Requires: R-RNetCDF-license = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : netcdf-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
for efficient storage of array-oriented scientific data and descriptions.
  Most capabilities of 'NetCDF' version 4 are supported. Optional conversions
  of time units are enabled by 'UDUNITS' version 2, also from Unidata.

%package lib
Summary: lib components for the R-RNetCDF package.
Group: Libraries
Requires: R-RNetCDF-license = %{version}-%{release}

%description lib
lib components for the R-RNetCDF package.


%package license
Summary: license components for the R-RNetCDF package.
Group: Default

%description license
license components for the R-RNetCDF package.


%prep
%setup -q -n RNetCDF
pushd ..
cp -a RNetCDF buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698073396

%install
export SOURCE_DATE_EPOCH=1698073396
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-RNetCDF
cp %{_builddir}/RNetCDF/COPYING %{buildroot}/usr/share/package-licenses/R-RNetCDF/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/RNetCDF/LICENSE %{buildroot}/usr/share/package-licenses/R-RNetCDF/53be8854eb9bea650b33bc5f0cfbb5100b0a0e31 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/RNetCDF/demo/Rmpi_writeN_read1.R
/usr/lib64/R/library/RNetCDF/demo/pbdMPI_writeN_read1.R
/usr/lib64/R/library/RNetCDF/help/AnIndex
/usr/lib64/R/library/RNetCDF/help/RNetCDF.rdb
/usr/lib64/R/library/RNetCDF/help/RNetCDF.rdx
/usr/lib64/R/library/RNetCDF/help/aliases.rds
/usr/lib64/R/library/RNetCDF/help/paths.rds
/usr/lib64/R/library/RNetCDF/html/00Index.html
/usr/lib64/R/library/RNetCDF/html/R.css
/usr/lib64/R/library/RNetCDF/libs/symbols.rds
/usr/lib64/R/library/RNetCDF/tests/RNetCDF-test.R
/usr/lib64/R/library/RNetCDF/udunits/udunits2.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RNetCDF/libs/RNetCDF.so
/usr/lib64/R/library/RNetCDF/libs/RNetCDF.so.avx2
/usr/lib64/R/library/RNetCDF/libs/RNetCDF.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-RNetCDF/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/R-RNetCDF/53be8854eb9bea650b33bc5f0cfbb5100b0a0e31
