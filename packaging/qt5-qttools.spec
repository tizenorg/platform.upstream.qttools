# The MIT License (MIT)
# 
# Copyright (c) 2013 Tomasz Olszak <olszak.tomasz@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This file is based on qttools.spec from Mer project
# http://merproject.org

%define keep_static 1
Name:       qt5-qttools
Summary:    Development tools for Qt
Version:    5.2.90+alpha
Release:    0
Group:      Base/Libraries
License:    LGPL-2.1+ or GPL-3.0
URL:        http://qt.digia.com
Source:     %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtprintsupport-devel
BuildRequires:  qt5-qtplatformsupport-devel
BuildRequires:  qt5-qtbootstrap-devel
BuildRequires:  qt5-qmake
BuildRequires:  qt5-tools
BuildRequires:  qt5-qtdbus-devel
BuildRequires:  pkgconfig(Qt5QmlDevTools)
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains additional tools for building Qt applications.

%package linguist
Summary:    The linguist tools
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description linguist
This package contains the linguist tool

%package pixeltool
Summary:    The pixeltool tool
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description pixeltool
This package contains the pixeltool tool

%package qdbus
Summary:    The qdbus and qdbusviewer tool
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qdbus
This package contains the qdbus and qdbusviewer tool

%package qtuitools
Summary:    The QtUiTools library
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtuitools
This package contains the QtUiTools library

%package qtuitools-devel
Summary:    Development files for QtUiTools
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
 
%description qtuitools-devel
This package contains the files necessary to develop
applications that use QtUiTools


%package qtclucene
Summary:    The QtCLucene library
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtclucene
This package contains the QtCLucene library

%package qtclucene-devel
Summary:    Development files for QtLucense
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
 
%description qtclucene-devel
This package contains the files necessary to develop
applications that use QtCLucene

%package qtdesigner
Summary: The Qt designer libraries
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%package qthelp
Summary:    The QtHelp library
Group:      Base/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qthelp
This package contains the QtHelp library

%package qthelp-devel
Summary:    Development files for QtHelp
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
 
%description qthelp-devel
This package contains the files necessary to develop
applications that use QtHelp

%description qtdesigner
This package contains the files necessary to develop
applications that use QtDesigner

%package qtdesigner-devel
Summary:    Development files for QtDesigner
Group:      Base/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
 
%description qtdesigner-devel
This package contains the files necessary to develop
applications that use QtDesigner



%prep
%setup -q -n %{name}-%{version}/qttools

%build
export QTDIR=/usr/share/qt5
touch .git
qmake -qt=5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%fdupes %{buildroot}%{_libdir}
%fdupes %{buildroot}%{_includedir}
%fdupes %{buildroot}%{_datadir}

#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%post qtuitools
/sbin/ldconfig
%postun qtuitools
/sbin/ldconfig

%post qthelp
/sbin/ldconfig
%postun qthelp
/sbin/ldconfig

%post qtclucene
/sbin/ldconfig
%postun qtclucene
/sbin/ldconfig

%post qtdesigner
/sbin/ldconfig
%postun qtdesigner
/sbin/ldconfig



%files
%defattr(-,root,root,-)

%files linguist
%defattr(-,root,root,-)
%{_qt5_bindir}/lconvert
%{_qt5_bindir}/linguist
%{_qt5_bindir}/qtpaths
%{_qt5_bindir}/lrelease
%{_qt5_bindir}/lupdate
%{_datadir}/qt5/phrasebooks
%{_libdir}/cmake/Qt5Linguist*

%files pixeltool
%defattr(-,root,root,-)
%{_qt5_bindir}/pixeltool

%files qdbus
%defattr(-,root,root,-)
%{_qt5_bindir}/qdbus
%{_qt5_bindir}/qdbusviewer

%files qtuitools
%defattr(-,root,root,-)

%files qtuitools-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtUiTools
%{_libdir}/libQt5UiTools.prl
%{_libdir}/libQt5UiTools.a
%{_libdir}/libQt5UiTools.la
%{_libdir}/pkgconfig/Qt5UiTools.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_uitools.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_uitools_private.pri
%{_libdir}/cmake/Qt5UiTools

%files qthelp
%defattr(-,root,root,-)
%{_libdir}/libQt5Help.so.*

%files qthelp-devel
%defattr(-,root,root,-)
%{_qt5_bindir}/assistant
%{_qt5_bindir}/qhelpgenerator
%{_qt5_bindir}/qcollectiongenerator
%{_qt5_bindir}/qhelpconverter
%{_includedir}/qt5/QtHelp
%{_libdir}/libQt5Help.prl
%{_libdir}/libQt5Help.la
%{_libdir}/libQt5Help.so
%{_libdir}/pkgconfig/Qt5Help.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_help.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_help_private.pri
%{_libdir}/cmake/Qt5Help

%files qtclucene
%defattr(-,root,root,-)
%{_libdir}/libQt5CLucene.so.*

%files qtclucene-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtCLucene
%{_libdir}/libQt5CLucene.prl
%{_libdir}/libQt5CLucene.la
%{_libdir}/libQt5CLucene.so
%{_libdir}/pkgconfig/Qt5CLucene.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_clucene_private.pri
 
%files qtdesigner
%defattr(-,root,root,-)
%{_qt5_bindir}/designer
%{_libdir}/libQt5Designer*.so.*

%files qtdesigner-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtDesigner
%{_includedir}/qt5/QtDesignerComponents
%{_libdir}/libQt5Designer*.so
%{_libdir}/libQt5Designer*.prl
%{_libdir}/libQt5Designer*.la
%{_libdir}/libQt5Designer*.prl
%{_datadir}/qt5/mkspecs/modules/qt_lib_designer*.pri
%{_libdir}/pkgconfig/Qt5Designer*.pc
%{_libdir}/cmake/Qt5Designer

#### No changelog section, separate $pkg.changes contains the history
