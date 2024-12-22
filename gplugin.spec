#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static libraries
#
Summary:	GPlugin plugin library
Summary(pl.UTF-8):	GPlugin - biblioteka wtyczek
Name:		gplugin
Version:	0.44.2
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.xz
# Source0-md5:	57783f9fa1ca5934b1b630d5331d7b17
URL:		https://keep.imfreedom.org/gplugin/gplugin/
# -std=c17
BuildRequires:	gcc >= 6:7
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.1}
BuildRequires:	glib2-devel >= 1:2.76.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk4-devel >= 4.10.0
BuildRequires:	help2man
# require highest lua version for which lgi module is available
BuildRequires:	lua51-devel >= 5.1.0
BuildRequires:	lua-lgi
BuildRequires:	meson >= 1.0.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	python3-pygobject3-devel >= 3.0.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.029
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
Requires:	glib2 >= 1:2.76.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPlugin is a GObject based library that implements a reusable plugin
system. It supports loading plugins in multiple other languages via
loaders. It relies heavily on GObjectIntrospection to expose its API
to the other languages.

%description -l pl.UTF-8
GPlugin to oparta na GObject biblioteka implementująca system wtyczek
wielokrotnego użytku. Obsługuje ładowanie wtyczek w wielu językach
poprzez wtyczki ładujące. Polega na GObjectIntrospection, aby
udostępnić API dla innych języków.

%package loader-lua
Summary:	Lua loader for GPlugin library
Summary(pl.UTF-8):	Wtyczka GPlugin ładująca wtyczki w języku Lua
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lua-lgi

%description loader-lua
Lua loader for GPlugin library.

%description loader-lua -l pl.UTF-8
Wtyczka GPlugin ładująca wtyczki w języku Lua.

%package loader-python3
Summary:	Python 3 loader for GPlugin library
Summary(pl.UTF-8):	Wtyczka GPlugin ładująca wtyczki w języku Python 3
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	python3-pygobject3 >= 3.0.0

%description loader-python3
Python 3 loader for GPlugin library.

%description loader-python3 -l pl.UTF-8
Wtyczka GPlugin ładująca wtyczki w języku Python 3.

%package devel
Summary:	Header files for GPlugin library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GPlugin
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.76.0

%description devel
Header files for GPlugin library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GPlugin.

%package static
Summary:	Static GPlugin library
Summary(pl.UTF-8):	Statyczna biblioteka GPlugin
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GPlugin library.

%description static -l pl.UTF-8
Statyczna biblioteka GPlugin.

%package -n vala-gplugin
Summary:	Vala API for GPlugin library
Summary(pl.UTF-8):	API języka Vala do biblioteki GPlugin
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description -n vala-gplugin
Vala API for GPlugin library.

%description -n vala-gplugin -l pl.UTF-8
API języka Vala do biblioteki GPlugin.

%package apidocs
Summary:	API documentation for GPlugin library
Summary(pl.UTF-8):	Dokumentacja API biblioteki GPlugin
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for GPlugin library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki GPlugin.

%package gtk4
Summary:	GPlugin Gtk4 library
Summary(pl.UTF-8):	Biblioteka GPlugin Gtk4
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk4 >= 4.10.0

%description gtk4
GTK4 integration for GPlugin library.

%description gtk4 -l pl.UTF-8
Integracja z GTK4 dla biblioteki GPlugin.

%package gtk4-devel
Summary:	Header files for GPlugin Gtk4 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GPlugin Gtk4
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk4 = %{version}-%{release}
Requires:	gtk4-devel >= 4.10.0

%description gtk4-devel
Header files for GPlugin Gtk4 library.

%description gtk4-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GPlugin Gtk4.

%package gtk4-static
Summary:	Static GPlugin Gtk4 library
Summary(pl.UTF-8):	Statyczna biblioteka GPlugin Gtk4
Group:		Development/Libraries
Requires:	%{name}-gtk4-devel = %{version}-%{release}

%description gtk4-static
Static GPlugin Gtk4 library.

%description gtk4-static -l pl.UTF-8
Statyczna biblioteka GPlugin Gtk4.

%package -n vala-gplugin-gtk4
Summary:	Vala API for GPlugin Gtk4 library
Summary(pl.UTF-8):	API języka Vala do biblioteki GPlugin Gtk4
Group:		Development/Libraries
Requires:	%{name}-gtk4-devel = %{version}-%{release}
Requires:	vala-gplugin = %{version}-%{release}
BuildArch:	noarch

%description -n vala-gplugin-gtk4
Vala API for GPlugin Gtk4 library.

%description -n vala-gplugin-gtk4 -l pl.UTF-8
API języka Vala do biblioteki GPlugin Gtk4.

%package gtk4-apidocs
Summary:	API documentation for GPlugin Gtk4 library
Summary(pl.UTF-8):	Dokumentacja API biblioteki GPlugin Gtk4
Group:		Documentation
BuildArch:	noarch

%description gtk4-apidocs
API documentation for GPlugin Gtk4 library.

%description gtk4-apidocs -l pl.UTF-8
Dokumentacja API biblioteki GPlugin Gtk4.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	%{!?with_apidocs:-Ddoc=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/gplugin* $RPM_BUILD_ROOT%{_gidocdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk4 -p /sbin/ldconfig
%postun	gtk4 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog HISTORY.md README.md
%attr(755,root,root) %{_bindir}/gplugin-query
%attr(755,root,root) %{_libdir}/libgplugin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgplugin.so.0
%{_libdir}/girepository-1.0/GPlugin-1.0.typelib
%dir %{_libdir}/gplugin
%{_mandir}/man1/gplugin-query.1*

%files loader-lua
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gplugin/gplugin-lua.so

%files loader-python3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gplugin/gplugin-python3.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgplugin.so
%{_includedir}/gplugin-1.0
%{_datadir}/gir-1.0/GPlugin-1.0.gir
%dir %{_datadir}/gplugin
%{_datadir}/gplugin/valgrind
%{_pkgconfigdir}/gplugin.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgplugin.a
%endif

%files -n vala-gplugin
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gplugin.deps
%{_datadir}/vala/vapi/gplugin.vapi

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/gplugin
%endif

%files gtk4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gplugin-gtk4-viewer
%attr(755,root,root) %{_libdir}/libgplugin-gtk4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgplugin-gtk4.so.0
%{_libdir}/girepository-1.0/GPluginGtk4-1.0.typelib
%{_mandir}/man1/gplugin-gtk4-viewer.1*

%files gtk4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgplugin-gtk4.so
%{_includedir}/gplugin-gtk4-1.0
%{_datadir}/gir-1.0/GPluginGtk4-1.0.gir
%{_pkgconfigdir}/gplugin-gtk4.pc

%if %{with static_libs}
%files gtk4-static
%defattr(644,root,root,755)
%{_libdir}/libgplugin-gtk4.a
%endif

%files -n vala-gplugin-gtk4
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gplugin-gtk4.deps
%{_datadir}/vala/vapi/gplugin-gtk4.vapi

%if %{with apidocs}
%files gtk4-apidocs
%defattr(644,root,root,755)
%{_gidocdir}/gplugin-gtk4
%endif
