#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-partd
Version  : 1.4.1
Release  : 45
URL      : https://files.pythonhosted.org/packages/a5/39/d13decd99a0d7e4bdde3ede536237ddf08c8c69bcedb4784fa26de649b47/partd-1.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/a5/39/d13decd99a0d7e4bdde3ede536237ddf08c8c69bcedb4784fa26de649b47/partd-1.4.1.tar.gz
Summary  : Appendable key-value storage
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-partd-license = %{version}-%{release}
Requires: pypi-partd-python = %{version}-%{release}
Requires: pypi-partd-python3 = %{version}-%{release}
Requires: pypi(locket)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(locket)
BuildRequires : pypi(toolz)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
PartD
=====
|Build Status| |Version Status|
Key-value byte store with appendable values

%package license
Summary: license components for the pypi-partd package.
Group: Default

%description license
license components for the pypi-partd package.


%package python
Summary: python components for the pypi-partd package.
Group: Default
Requires: pypi-partd-python3 = %{version}-%{release}

%description python
python components for the pypi-partd package.


%package python3
Summary: python3 components for the pypi-partd package.
Group: Default
Requires: python3-core
Provides: pypi(partd)
Requires: pypi(locket)
Requires: pypi(toolz)

%description python3
python3 components for the pypi-partd package.


%prep
%setup -q -n partd-1.4.1
cd %{_builddir}/partd-1.4.1
pushd ..
cp -a partd-1.4.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695742862
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-partd
cp %{_builddir}/partd-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-partd/395d3fcb94348847e3b7afbfbdae2adeb0d6ec00 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-partd/395d3fcb94348847e3b7afbfbdae2adeb0d6ec00

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
