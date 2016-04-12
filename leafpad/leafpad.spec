Name:           leafpad
Version:        0.8.17
Release:        0.docs.1%{?dist}
Summary:        A GTK+ based simple text editor.

Group:			Application/Editors
License:        GPL
URL:            http://tarot.freeshell.org/leafpad
Source0:        http://savannah.nongnu.org/download/leafpad/leafpad-0.8.17.tar.gz

BuildRequires:  gtk2-devel >= 2.0
BuildRequires:	gettext-devel
# Requires:       gettext

%description
Leafpad is a simple GTK+ text editor that emphasizes simplicity.  As
development focuses on keeping weight down to a minimum, only the most
essential features are implemented in the editor.

%prep
%setup -q


%build
%configure
make %{?_smp_flags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang leafpad

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
# %defattr(-,root,root,-r)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/leafpad
%{_datadir}/applications/leafpad.desktop
%{_datadir}/icons/hicolor/16x16/apps/leafpad.png
%{_datadir}/icons/hicolor/22x22/apps/leafpad.png
%{_datadir}/icons/hicolor/24x24/apps/leafpad.png
%{_datadir}/icons/hicolor/32x32/apps/leafpad.png
%{_datadir}/icons/hicolor/scalable/apps/leafpad.svg
%{_datadir}/pixmaps/leafpad.png
%{_datadir}/pixmaps/leafpad.xpm

%changelog
* Tue Apr 12 2016 Erin M Gunn ikonone@gmail.com 0.8.17-0.docs.1
- Initial RPM release
