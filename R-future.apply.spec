#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v5
# autospec commit: c02b2fe
#
Name     : R-future.apply
Version  : 1.11.2
Release  : 18
URL      : https://cran.r-project.org/src/contrib/future.apply_1.11.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/future.apply_1.11.2.tar.gz
Summary  : Apply Function to Elements in Parallel using Futures
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-future
Requires: R-globals
BuildRequires : R-future
BuildRequires : R-globals
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n future.apply
pushd ..
cp -a future.apply buildavx2
popd
pushd ..
cp -a future.apply buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711729904

%install
export SOURCE_DATE_EPOCH=1711729904
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/future.apply/CITATION
/usr/lib64/R/library/future.apply/DESCRIPTION
/usr/lib64/R/library/future.apply/INDEX
/usr/lib64/R/library/future.apply/Meta/Rd.rds
/usr/lib64/R/library/future.apply/Meta/features.rds
/usr/lib64/R/library/future.apply/Meta/hsearch.rds
/usr/lib64/R/library/future.apply/Meta/links.rds
/usr/lib64/R/library/future.apply/Meta/nsInfo.rds
/usr/lib64/R/library/future.apply/Meta/package.rds
/usr/lib64/R/library/future.apply/Meta/vignette.rds
/usr/lib64/R/library/future.apply/NAMESPACE
/usr/lib64/R/library/future.apply/NEWS.md
/usr/lib64/R/library/future.apply/R/future.apply
/usr/lib64/R/library/future.apply/R/future.apply.rdb
/usr/lib64/R/library/future.apply/R/future.apply.rdx
/usr/lib64/R/library/future.apply/WORDLIST
/usr/lib64/R/library/future.apply/doc/future.apply-1-overview.html
/usr/lib64/R/library/future.apply/doc/future.apply-1-overview.md.rsp
/usr/lib64/R/library/future.apply/doc/index.html
/usr/lib64/R/library/future.apply/help/AnIndex
/usr/lib64/R/library/future.apply/help/aliases.rds
/usr/lib64/R/library/future.apply/help/future.apply.rdb
/usr/lib64/R/library/future.apply/help/future.apply.rdx
/usr/lib64/R/library/future.apply/help/paths.rds
/usr/lib64/R/library/future.apply/html/00Index.html
/usr/lib64/R/library/future.apply/html/R.css
/usr/lib64/R/library/future.apply/tests/fold.R
/usr/lib64/R/library/future.apply/tests/future_apply.R
/usr/lib64/R/library/future.apply/tests/future_by.R
/usr/lib64/R/library/future.apply/tests/future_eapply.R
/usr/lib64/R/library/future.apply/tests/future_lapply,RNG.R
/usr/lib64/R/library/future.apply/tests/future_lapply,globals.R
/usr/lib64/R/library/future.apply/tests/future_lapply.R
/usr/lib64/R/library/future.apply/tests/future_mapply,globals.R
/usr/lib64/R/library/future.apply/tests/future_mapply.R
/usr/lib64/R/library/future.apply/tests/future_replicate.R
/usr/lib64/R/library/future.apply/tests/future_sapply.R
/usr/lib64/R/library/future.apply/tests/future_tapply.R
/usr/lib64/R/library/future.apply/tests/future_vapply.R
/usr/lib64/R/library/future.apply/tests/globals,tricky_recursive.R
/usr/lib64/R/library/future.apply/tests/incl/end.R
/usr/lib64/R/library/future.apply/tests/incl/start,load-only.R
/usr/lib64/R/library/future.apply/tests/incl/start.R
/usr/lib64/R/library/future.apply/tests/options,nested.R
/usr/lib64/R/library/future.apply/tests/rng.R
/usr/lib64/R/library/future.apply/tests/startup.Rs
/usr/lib64/R/library/future.apply/tests/stdout.R
/usr/lib64/R/library/future.apply/tests/utils.R
