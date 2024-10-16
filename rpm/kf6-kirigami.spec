%global  kf_version 6.6.0

Name:           kf6-kirigami
Version: 6.6.0
Release:        0%{?dist}
Summary:        QtQuick plugins to build user interfaces based on the KDE UX guidelines
License:        BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:            https://invent.kde.org/frameworks/%{framework}
Source0: %{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  kf6-extra-cmake-modules >= %{majmin_ver_kf6}
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qt6-qttools-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 libkirigami6_qt

%files -f libkirigami6_qt.lang
%doc README.md
%dir %{_kf6_qmldir}/org/
%dir %{_kf6_qmldir}/org/kde/
%license LICENSES/*.txt
%license templates/kirigami6/LICENSES/*.txt
%{_kf6_qmldir}/org/kde/kirigami
%{_datadir}/qlogging-categories6/kirigami.categories
%{_kf6_libdir}/libKirigami.so.*
%{_kf6_libdir}/libKirigamiDelegates.so.*
%{_kf6_libdir}/libKirigamiDialogs.so.*
%{_kf6_libdir}/libKirigamiLayouts.so.*
%{_kf6_libdir}/libKirigamiPlatform.so.*
%{_kf6_libdir}/libKirigamiPrimitives.so.*
%{_kf6_libdir}/libKirigamiPrivate.so.*

%files devel
%dir %{_kf6_datadir}/kdevappwizard/
%dir %{_kf6_datadir}/kdevappwizard/templates/
%{_kf6_datadir}/kdevappwizard/templates/kirigami6.tar.bz2
%{_kf6_includedir}/Kirigami/
%{_kf6_libdir}/cmake/KF6Kirigami{,2}/
%{_kf6_libdir}/cmake/KF6KirigamiPlatform/
%{_kf6_libdir}/libKirigami.so
%{_kf6_libdir}/libKirigamiDelegates.so
%{_kf6_libdir}/libKirigamiDialogs.so
%{_kf6_libdir}/libKirigamiLayouts.so
%{_kf6_libdir}/libKirigamiPlatform.so
%{_kf6_libdir}/libKirigamiPrimitives.so
%{_kf6_libdir}/libKirigamiPrivate.so
%{_qt6_docdir}/*.tags


%files doc
%{_qt6_docdir}/*.qch
