#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libwebp
Version  : 1.2.1
Release  : 38
URL      : https://github.com/webmproject/libwebp/archive/v1.2.1/libwebp-1.2.1.tar.gz
Source0  : https://github.com/webmproject/libwebp/archive/v1.2.1/libwebp-1.2.1.tar.gz
Summary  : Library for the WebP graphics format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libwebp-bin = %{version}-%{release}
Requires: libwebp-filemap = %{version}-%{release}
Requires: libwebp-lib = %{version}-%{release}
Requires: libwebp-license = %{version}-%{release}
Requires: libwebp-man = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : freeglut-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libjpeg-turbo-dev32
BuildRequires : libpng-dev32
BuildRequires : mesa-dev32
BuildRequires : sed
BuildRequires : tiff-dev

%description
__   __  ____  ____  ____
/  \\/  \/  _ \/  _ )/  _ \
\       /   __/  _  \   __/
\__\__/\____/\_____/__/ ____  ___
/ _/ /    \    \ /  _ \/ _/
/  \_/   / /   \ \   __/  \__
\____/____/\_____/_____/____/v1.2.1

%package bin
Summary: bin components for the libwebp package.
Group: Binaries
Requires: libwebp-license = %{version}-%{release}
Requires: libwebp-filemap = %{version}-%{release}

%description bin
bin components for the libwebp package.


%package dev
Summary: dev components for the libwebp package.
Group: Development
Requires: libwebp-lib = %{version}-%{release}
Requires: libwebp-bin = %{version}-%{release}
Provides: libwebp-devel = %{version}-%{release}
Requires: libwebp = %{version}-%{release}

%description dev
dev components for the libwebp package.


%package dev32
Summary: dev32 components for the libwebp package.
Group: Default
Requires: libwebp-lib32 = %{version}-%{release}
Requires: libwebp-bin = %{version}-%{release}
Requires: libwebp-dev = %{version}-%{release}

%description dev32
dev32 components for the libwebp package.


%package filemap
Summary: filemap components for the libwebp package.
Group: Default

%description filemap
filemap components for the libwebp package.


%package lib
Summary: lib components for the libwebp package.
Group: Libraries
Requires: libwebp-license = %{version}-%{release}
Requires: libwebp-filemap = %{version}-%{release}

%description lib
lib components for the libwebp package.


%package lib32
Summary: lib32 components for the libwebp package.
Group: Default
Requires: libwebp-license = %{version}-%{release}

%description lib32
lib32 components for the libwebp package.


%package license
Summary: license components for the libwebp package.
Group: Default

%description license
license components for the libwebp package.


%package man
Summary: man components for the libwebp package.
Group: Default

%description man
man components for the libwebp package.


%prep
%setup -q -n libwebp-1.2.1
cd %{_builddir}/libwebp-1.2.1
pushd ..
cp -a libwebp-1.2.1 build32
popd
pushd ..
cp -a libwebp-1.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633828540
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
%autogen --disable-static --enable-libwebpdemux \
--enable-libwebpmux
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen --disable-static --enable-libwebpdemux \
--enable-libwebpmux --disable-gl --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%autogen --disable-static --enable-libwebpdemux \
--enable-libwebpmux
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1633828540
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libwebp
cp %{_builddir}/libwebp-1.2.1/COPYING %{buildroot}/usr/share/package-licenses/libwebp/59cd938fcbd6735b1ef91781280d6eb6c4b7c5d9
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cwebp
/usr/bin/dwebp
/usr/bin/img2webp
/usr/bin/webpinfo
/usr/bin/webpmux
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/webp/decode.h
/usr/include/webp/demux.h
/usr/include/webp/encode.h
/usr/include/webp/mux.h
/usr/include/webp/mux_types.h
/usr/include/webp/types.h
/usr/lib64/libwebp.so
/usr/lib64/libwebpdemux.so
/usr/lib64/libwebpmux.so
/usr/lib64/pkgconfig/libwebp.pc
/usr/lib64/pkgconfig/libwebpdemux.pc
/usr/lib64/pkgconfig/libwebpmux.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libwebp.so
/usr/lib32/libwebpdemux.so
/usr/lib32/libwebpmux.so
/usr/lib32/pkgconfig/32libwebp.pc
/usr/lib32/pkgconfig/32libwebpdemux.pc
/usr/lib32/pkgconfig/32libwebpmux.pc
/usr/lib32/pkgconfig/libwebp.pc
/usr/lib32/pkgconfig/libwebpdemux.pc
/usr/lib32/pkgconfig/libwebpmux.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-libwebp

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwebp.so.7
/usr/lib64/libwebp.so.7.1.2
/usr/lib64/libwebpdemux.so.2
/usr/lib64/libwebpdemux.so.2.0.8
/usr/lib64/libwebpmux.so.3
/usr/lib64/libwebpmux.so.3.0.7
/usr/share/clear/optimized-elf/lib*

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libwebp.so.7
/usr/lib32/libwebp.so.7.1.2
/usr/lib32/libwebpdemux.so.2
/usr/lib32/libwebpdemux.so.2.0.8
/usr/lib32/libwebpmux.so.3
/usr/lib32/libwebpmux.so.3.0.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libwebp/59cd938fcbd6735b1ef91781280d6eb6c4b7c5d9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cwebp.1
/usr/share/man/man1/dwebp.1
/usr/share/man/man1/img2webp.1
/usr/share/man/man1/webpinfo.1
/usr/share/man/man1/webpmux.1
