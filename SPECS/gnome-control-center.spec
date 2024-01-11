%define gnome_online_accounts_version 3.25.3
%define glib2_version 2.56.0
%define gnome_desktop_version 3.35.4
%define gsd_version 3.35.0
%define gsettings_desktop_schemas_version 3.37.1
%define upower_version 0.99.8
%define gtk3_version 3.22.20
%define cheese_version 3.28.0
%define gnome_bluetooth_version 3.18.2
%define nm_version 1.24
%define power_profiles_daemon_version 0.9.0

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-control-center
Version:        40.0
Release:        29%{?dist}
Summary:        Utilities to configure the GNOME desktop

License:        GPLv2+ and CC-BY-SA
URL:            http://www.gnome.org
Source0:        https://download.gnome.org/sources/gnome-control-center/40/gnome-control-center-%{tarball_version}.tar.xz

# https://gitlab.gnome.org/GNOME/gnome-control-center/-/merge_requests/965
Patch0:         distro-logo.patch

# Customized for RHEL 9 to skip the .gitlab-ci.yml file
# https://gitlab.gnome.org/GNOME/gnome-control-center/-/issues/1345
# https://bugzilla.redhat.com/show_bug.cgi?id=1952274
Patch1:         gnome-control-center-Drop-the-unused-build-dependency-on-Grilo.patch
Patch2:         power-profiles-backport.patch
Patch3:         wwan-backport-gnome-40.patch
Patch4:         subscription-manager-support.patch
Patch5:         application-use-icon-name-that-exists.patch
Patch6:         backport-multitasking-panel.patch
Patch7:         rpminspect-desktop-fixes.patch

# Backport monitor config policy (#2046159)
Patch8:         0001-display-Only-display-configuration-options-if-apply-.patch

# Workaround for libnma not handling OWE https://gitlab.gnome.org/GNOME/libnma/-/issues/9
Patch9:         0001-network-Fix-OWE-settings.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2097838
Patch10:        gnome-control-center-timezones.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2061182
Patch11:        change-device-name-with-enter-key.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2057154
Patch12:        display-infobar-if-night-light-unsupported.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2110581
Patch13:        gnome-control-center-wwan-5g-support.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2168686
Patch14:        0001-shell-Avoid-handling-map-events-from-other-windows.patch

BuildRequires:  chrpath
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl libxslt
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese) >= %{cheese_version}
BuildRequires:  pkgconfig(cheese-gtk)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_desktop_version}
BuildRequires:  pkgconfig(gnome-settings-daemon) >= %{gsd_version}
BuildRequires:  pkgconfig(goa-1.0) >= %{gnome_online_accounts_version}
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gsettings_desktop_schemas_version}
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnm) >= %{nm_version}
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(upower-glib) >= %{upower_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(gcr-3)
%ifnarch s390 s390x
BuildRequires:  pkgconfig(gnome-bluetooth-1.0) >= %{gnome_bluetooth_version}
BuildRequires:  pkgconfig(libwacom)
%endif

# Versioned library deps
Requires: cheese-libs%{?_isa} >= %{cheese_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gnome-desktop3%{?_isa} >= %{gnome_desktop_version}
Requires: gnome-online-accounts%{?_isa} >= %{gnome_online_accounts_version}
Requires: gnome-settings-daemon%{?_isa} >= %{gsd_version}
# For g-s-d subscription manager patches
Requires: gnome-settings-daemon%{?_isa} >= 40.0.1-4
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: upower%{?_isa} >= %{upower_version}
Requires: power-profiles-daemon >= %{power_profiles_daemon_version}
%ifnarch s390 s390x
Requires: gnome-bluetooth%{?_isa} >= 1:%{gnome_bluetooth_version}
%endif

Requires: %{name}-filesystem = %{version}-%{release}
# For user accounts
Requires: accountsservice
Requires: alsa-lib
# For the thunderbolt panel
Recommends: bolt
# For the color panel
Requires: colord
# For the printers panel
Requires: cups-pk-helper
Requires: dbus
# For the info/details panel
Requires: glx-utils
# For the user languages
Requires: iso-codes
# For the network panel
Recommends: NetworkManager-wifi
Recommends: nm-connection-editor
# For Show Details in the color panel
Recommends: gnome-color-manager
# For the sharing panel
Recommends: gnome-remote-desktop
%if 0%{?fedora}
Recommends: rygel
%endif
# For the info/details panel
Recommends: switcheroo-control
# For the keyboard panel
Requires: /usr/bin/gkbd-keyboard-display
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 9
# For the power panel
Recommends: power-profiles-daemon
%endif

# Renamed in F28
Provides: control-center = 1:%{version}-%{release}
Provides: control-center%{?_isa} = 1:%{version}-%{release}
Obsoletes: control-center < 1:%{version}-%{release}

%description
This package contains configuration utilities for the GNOME desktop, which
allow to configure accessibility options, desktop fonts, keyboard and mouse
properties, sound setup, desktop theme and background, user interface
properties, screen resolution, and other settings.

%package filesystem
Summary: GNOME Control Center directories
# NOTE: this is an "inverse dep" subpackage. It gets pulled in
# NOTE: by the main package and MUST not depend on the main package
BuildArch: noarch
# Renamed in F28
Provides: control-center-filesystem = 1:%{version}-%{release}
Obsoletes: control-center-filesystem < 1:%{version}-%{release}

%description filesystem
The GNOME control-center provides a number of extension points
for applications. This package contains directories where applications
can install configuration files that are picked up by the control-center
utilities.

%prep
%autosetup -Sgit -p1 -n gnome-control-center-%{tarball_version}

%build
%meson \
  -Ddocumentation=true \
%if 0%{?fedora}
  -Ddistributor_logo=%{_datadir}/pixmaps/fedora_logo_med.png \
  -Ddark_mode_distributor_logo=%{_datadir}/pixmaps/fedora_whitelogo_med.png \
%endif
%if 0%{?rhel}
  -Ddistributor_logo=%{_datadir}/pixmaps/fedora-logo.png \
  -Ddark_mode_distributor_logo=%{_datadir}/pixmaps/system-logo-white.png \
%endif
  %{nil}
%meson_build

%install
%meson_install

# We do want this
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

# We don't want these
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/autostart
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/cursor-fonts

# Remove rpath
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/gnome-control-center

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%{_bindir}/gnome-control-center
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/gnome-control-center
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.SearchProvider.service
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.service
%{_datadir}/gettext/
%{_datadir}/glib-2.0/schemas/org.gnome.ControlCenter.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_datadir}/gnome-control-center/pixmaps
%{_datadir}/gnome-shell/search-providers/gnome-control-center-search-provider.ini
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/man/man1/gnome-control-center.1*
%{_datadir}/metainfo/gnome-control-center.appdata.xml
%{_datadir}/pixmaps/faces
%{_datadir}/pkgconfig/gnome-keybindings.pc
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.*.policy
%{_datadir}/polkit-1/rules.d/gnome-control-center.rules
%{_datadir}/sounds/gnome/default/*/*.ogg
%{_libexecdir}/cc-remote-login-helper
%{_libexecdir}/gnome-control-center-search-provider
%{_libexecdir}/gnome-control-center-print-renderer

%files filesystem
%dir %{_datadir}/gnome-control-center
%dir %{_datadir}/gnome-control-center/keybindings
%dir %{_datadir}/gnome/wm-properties

%changelog
* Fri Feb 10 2023 Felipe Borges <feborges@redhat.com> - 40.0-29
- Fix keyboard accessibility of screen resolution list
  Resolves: rhbz#2168686

* Wed Oct 26 2022 Felipe Borges <feborges@redhat.com> - 40.0-28
- Support WWAN 5G connections
  Resolves: rhbz#2110581

* Mon Aug 01 2022 Felipe Borges <feborges@redhat.com> - 40.0-27
- Show infobar if night light isn't supported
  Resolves: rhbz#2057154

* Mon Aug 01 2022 Felipe Borges <feborges@redhat.com> - 40.0-26
- Allow changing "Device Name" by pressing "Enter"
  Resolves: rhbz#2061182

* Fri Jul 08 2022 Felipe Borges <feborges@redhat.com> - 40.0-25
- Backport translations for Multitasking panel
- Make Multitasking panel capable of handling Right-to-Left locales
  Resolves: #2105228

* Wed Jun 22 2022 Tomas Popela <tpopela@redhat.com> - 40.0-24
- Bump the release to fix upgrades
- Related: rhbz#2097838

* Wed Jun 22 2022 Tomas Popela <tpopela@redhat.com> - 40.0-23
- Remove timezone boundaries
- Resolves: rhbz#2097838

* Thu Feb 24 2022 Benjamin Berg <bberg@redhat.com> - 40.0-22
- Work around libnma not handling OWE
  Resolves: #2058163

* Fri Feb 04 2022 Jonas Ådahl <tpopela@redhat.com> - 40.0-21
- Backport monitor config policy
  Resolves: #2046159

* Wed Feb 02 2022 Tomas Popela <tpopela@redhat.com> - 40.0-20
- Fix rpminspect desktop files warnings
- Resolves: #2041348

* Fri Jan 28 2022 Felipe Borges <feborges@redhat.com> - 40.0-19
- Backport Multitasking panel
- Resolves: #2047723

* Thu Jan 20 2022 Felipe Borges <feborges@redhat.com> - 40.0-18
- Fix typo in the previous patch
- Resolves: #2041348

* Fri Jan 14 2022 Felipe Borges <feborges@redhat.com> - 40.0-17
- Set an existing Icon name in the Applications' panel desktop file
- Resolves: #2041348

* Tue Sep 07 2021 Kalev Lember <klember@redhat.com> - 40.0-16
- Add desktop file keywords for subscription support
- Resolves: #1937113

* Thu Sep 02 2021 Kalev Lember <klember@redhat.com> - 40.0-15
- Forward port subscription manager support from RHEL 8
- Resolves: #1937113

* Wed Aug 25 2021 Carlos Garnacho <cgarnach@redhat.com> - 40.0-14
- Backport WWAN panel
  Resolves: #1995559

* Fri Aug 20 2021 Carlos Garnacho <cgarnach@redhat.com> - 40.0.13
- Backport power profile changes
  Resolves: #1994475

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 40.0-12
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Apr 27 2021 Debarshi Ray <rishi@fedoraproject.org> - 40.0-11
- Drop the unused build dependency on Grilo
Resolves: #1952274

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 40.0-10
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Apr 02 2021 Kalev Lember <klember@redhat.com> - 40.0-9
- Only enable power-profiles-daemon on F35+ and RHEL 9+

* Wed Mar 31 2021 Pete Walter <pwalter@fedoraproject.org> - 40.0-8
- Add back power-profiles-daemon once more

* Wed Mar 31 2021 Michael Catanzaro <mcatanzaro@redhat.com> - 40.0-7
- Drop Recommends: power-profiles-daemon for F34

* Tue Mar 30 2021 Pete Walter <pwalter@fedoraproject.org> - 40.0-6
- Use recommends for a few more things

* Tue Mar 30 2021 Bastien Nocera <bnocera@redhat.com> - 40.0-4
- Drag power-profiles-daemon in for the power panel

* Mon Mar 29 2021 Michael Catanzaro <mcatanzaro@redhat.com> - 40.0-3
- Update Fedora logos to larger versions

* Wed Mar 24 2021 Kalev Lember <klember@redhat.com> - 40.0-2
- Rebuilt

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 40~rc-1
- Update to 40.rc

* Wed Mar 10 2021 Michael Catanzaro <mcatanzaro@redhat.com> - 40~beta-5
- Refresh distro logo patch
- Drop Recommends: vino, let vino die!

* Sun Mar 07 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 40~beta-4
- Fix modifications of the networks (Fixes: RHBZ#1932674)

* Wed Feb 24 2021 Felipe Borges <feborges@redhat.com> - 40~beta-3
- Include missing patch from 40~beta-2

* Tue Feb 23 2021 Felipe Borges <feborges@redhat.com> - 40~beta-2
- Fix error preventing the Region & Language panel from loading

* Sun Feb 21 2021 Kalev Lember <klember@redhat.com> - 40~beta-1
- Update to 40.beta

* Mon Feb 15 2021 Kalev Lember <klember@redhat.com> - 3.38.4-1
- Update to 3.38.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kalev Lember <klember@redhat.com> - 3.38.3-1
- Update to 3.38.3

* Fri Nov 20 2020 Kalev Lember <klember@redhat.com> - 3.38.2-2
- search: Check for either tracker 2.x or 3.x schemas

* Fri Nov 20 2020 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Tue Oct 13 2020 Kalev Lember <klember@redhat.com> - 3.38.1-2
- Add Recommends: nm-connection-editor for the network panel (#1887891)

* Mon Oct  5 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Sat Sep 19 2020 Yaroslav Fedevych <yaroslav@fedevych.name> - 3.38.0-2
- Specify the minimum libnm version needed to build the package

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sun Sep 06 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Tue Aug 04 2020 Michael Catanzaro <mcatanzaro@redhat.com> - 3.37.3-4
- Add Recommends: gnome-color-manager for the color panel

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 3.37.3-1
- Update to 3.37.3

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 3.36.4-1
- Update to 3.36.4

* Wed Jun 03 2020 Kalev Lember <klember@redhat.com> - 3.36.3-1
- Update to 3.36.3

* Fri May 01 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Tue Apr 28 2020 Felipe Borges <feborges@redhat.com> - 3.36.1-2
- Add "Model" row info for Lenovo devices

* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Thu Mar 19 2020 Michael Catanzaro <mcatanzaro@redhat.com> - 3.36.0-3
- No changes, bump revision to maintain upgrade path from F32

* Mon Mar 16 2020 Michael Catanzaro <mcatanzaro@redhat.com> - 3.36.0-2
- Update distro-logo.patch to use fedora_vertical version of logo.

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Mar 02 2020 Kalev Lember <klember@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Mon Feb 03 2020 Bastien Nocera <bnocera@redhat.com> - 3.35.90-1
+ gnome-control-center-3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 3.34.2-3
- Backport a patch to fix the build with latest libgnome-desktop

* Mon Dec 09 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.34.2-2
- Drop nm-connection-editor requires, per gnome-control-center#512
- To edit mobile broadband connections, install nm-connection-editor

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Thu Oct 10 2019 Adam Williamson <awilliam@redhat.com> - 3.34.1-4
- Add patch to fix crash when selecting display with no modes (rhbz#1756553)

* Wed Oct 09 2019 Felipe Borges <feborges@redhat.com> - 3.34.1-3
- Add patch to fix parsing of addresses while adding printers (rhbz#1750394)

* Mon Oct 07 2019 Benjamin Berg <bberg@redhat.com> - 3.34.1-2
- Add patch to fix resetting of system wide format locale (rhbz#1759221)

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Sat Oct 05 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.34.0.1-3
- Add patch to fix editing wired connection settings (rhbz#1750805)
- Remove broken remote printers patch

* Wed Oct 02 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.34.0.1-2
- Add patch to fix crash when configuring remote printers

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0.1-1
- Update to 3.34.0.1

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Kalev Lember <klember@redhat.com> - 3.33.3-2
- Remove libXxf86misc-devel BuildRequires as the package no longer exists

* Wed Jun 19 2019 Kalev Lember <klember@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Fri May 24 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.1-2
- Rebuild with Meson fix for #1699099

* Fri Mar 29 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0.1-1
- Update to 3.32.0.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Mon Mar 04 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Sat Feb 23 2019 Kevin Fenzi <kevin@scrye.com> - 3.31.90-2
- Add https://gitlab.gnome.org/GNOME/gnome-control-center/merge_requests/387.patch 
  to fix udisks crash

* Thu Feb 07 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4

* Tue Nov 20 2018 Pete Walter <pwalter@fedoraproject.org> - 3.30.2-3
- Recommend gnome-remote-desktop for the sharing panel

* Sat Nov 17 2018 Pete Walter <pwalter@fedoraproject.org> - 3.30.2-2
- Change bolt requires to recommends (#1643709)
- Change rygel requires to recommends

* Thu Nov 01 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2

* Thu Oct 11 2018 David Herrmann <dh.herrmann@gmail.com> - 3.30.1-4
- Reduce 'dbus-x11' dependency to 'dbus'. The xinit scripts are no longer the
  canonical way to start dbus, but the 'dbus' package is nowadays required to
  provide a user and system bus to its dependents.

* Wed Oct 10 2018 Benjamin Berg <bberg@redhat.com> - 3.30.1-3
- Add patch to improve background loading. The patch is not acceptable
  upstream as is, but is also a good improvement on the current situation
  (#1631002)

* Sun Oct 07 2018 Kalev Lember <klember@redhat.com> - 3.30.1-2
- Backport an upstream fix for a crash in the online accounts panel

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Sun Aug 12 2018 Kalev Lember <klember@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Wed May 23 2018 Pete Walter <pwalter@fedoraproject.org> - 3.28.1-4
- Change NetworkManager-wifi requires to recommends (#1478661)

* Tue May 22 2018 Ray Strode <rstrode@redhat.com> - 3.28.1-3
- Change vino requires to a vino recommends

* Fri Apr 13 2018 Kalev Lember <klember@redhat.com> - 3.28.1-2
- Backport new thunderbolt panel

* Tue Apr 10 2018 Pete Walter <pwalter@fedoraproject.org> - 3.28.1-1
- Rename control-center to gnome-control-center
