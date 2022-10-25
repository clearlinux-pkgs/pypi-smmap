#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-smmap
Version  : 5.0.0
Release  : 29
URL      : https://files.pythonhosted.org/packages/21/2d/39c6c57032f786f1965022563eec60623bb3e1409ade6ad834ff703724f3/smmap-5.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/2d/39c6c57032f786f1965022563eec60623bb3e1409ade6ad834ff703724f3/smmap-5.0.0.tar.gz
Summary  : A pure Python implementation of a sliding window memory map manager
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-smmap-license = %{version}-%{release}
Requires: pypi-smmap-python = %{version}-%{release}
Requires: pypi-smmap-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
When reading from many possibly large files in a fashion similar to random access, it is usually the fastest and most efficient to use memory maps.
        
        Although memory maps have many advantages, they represent a very limited system resource as every map uses one file descriptor, whose amount is limited per process. On 32 bit systems, the amount of memory you can have mapped at a time is naturally limited to theoretical 4GB of memory, which may not be enough for some applications.
        
        
        ## Limitations
        
        * **System resources (file-handles) are likely to be leaked!** This is due to the library authors reliance on a deterministic `__del__()` destructor.
        * The memory access is read-only by design.
        
        
        ## Overview

%package license
Summary: license components for the pypi-smmap package.
Group: Default

%description license
license components for the pypi-smmap package.


%package python
Summary: python components for the pypi-smmap package.
Group: Default
Requires: pypi-smmap-python3 = %{version}-%{release}

%description python
python components for the pypi-smmap package.


%package python3
Summary: python3 components for the pypi-smmap package.
Group: Default
Requires: python3-core
Provides: pypi(smmap)

%description python3
python3 components for the pypi-smmap package.


%prep
%setup -q -n smmap-5.0.0
cd %{_builddir}/smmap-5.0.0
pushd ..
cp -a smmap-5.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656408179
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-smmap
cp %{_builddir}/smmap-5.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-smmap/62b7f6262d13a59f19d9e458820dd16f5bd99358
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
/usr/share/package-licenses/pypi-smmap/62b7f6262d13a59f19d9e458820dd16f5bd99358

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
