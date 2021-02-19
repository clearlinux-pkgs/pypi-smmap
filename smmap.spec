#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : smmap
Version  : 4.0.0
Release  : 12
URL      : https://files.pythonhosted.org/packages/dd/d4/2b4f196171674109f0fbb3951b8beab06cd0453c1b247ec0c4556d06648d/smmap-4.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/dd/d4/2b4f196171674109f0fbb3951b8beab06cd0453c1b247ec0c4556d06648d/smmap-4.0.0.tar.gz
Summary  : A pure Python implementation of a sliding window memory map manager
Group    : Development/Tools
License  : BSD-3-Clause
Requires: smmap-license = %{version}-%{release}
Requires: smmap-python = %{version}-%{release}
Requires: smmap-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : nosexcover
BuildRequires : nosexcover-python

%description
When reading from many possibly large files in a fashion similar to random access, it is usually the fastest and most efficient to use memory maps.
        
        Although memory maps have many advantages, they represent a very limited system resource as every map uses one file descriptor, whose amount is limited per process. On 32 bit systems, the amount of memory you can have mapped at a time is naturally limited to theoretical 4GB of memory, which may not be enough for some applications.
        
        
        ## Limitations
        
        * **System resources (file-handles) are likely to be leaked!** This is due to the library authors reliance on a deterministic `__del__()` destructor.
        * The memory access is read-only by design.
        
        
        ## Overview

%package license
Summary: license components for the smmap package.
Group: Default

%description license
license components for the smmap package.


%package python
Summary: python components for the smmap package.
Group: Default
Requires: smmap-python3 = %{version}-%{release}

%description python
python components for the smmap package.


%package python3
Summary: python3 components for the smmap package.
Group: Default
Requires: python3-core
Provides: pypi(smmap)

%description python3
python3 components for the smmap package.


%prep
%setup -q -n smmap-4.0.0
cd %{_builddir}/smmap-4.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611676980
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/smmap
cp %{_builddir}/smmap-4.0.0/LICENSE %{buildroot}/usr/share/package-licenses/smmap/62b7f6262d13a59f19d9e458820dd16f5bd99358
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/smmap/62b7f6262d13a59f19d9e458820dd16f5bd99358

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
