%define gnome_online_accounts_version 3.25.3
%define glib2_version 2.53.0
%define gnome_desktop_version 3.27.90
%define gsd_version 3.32.0-13

%define gsettings_desktop_schemas_version 3.27.2
%define gtk3_version 3.22.20
%define upower_version 0.99.6
%define cheese_version 3.28.0
%define gnome_bluetooth_version 3.18.2

Name:           gnome-control-center
Version:        3.28.2
Release:        37%{?dist}
Summary:        Utilities to configure the GNOME desktop

License:        GPLv2+ and CC-BY-SA
URL:            http://www.gnome.org
Source0:        https://download.gnome.org/sources/gnome-control-center/3.28/gnome-control-center-%{version}.tar.xz

# https://bugzilla.gnome.org/show_bug.cgi?id=695691
Patch0:         distro-logo.patch

# thunderbolt panel backported to 3.28.x
# https://gitlab.gnome.org/gicmo/gnome-control-center/commits/thunderbolt_3_28_1
Patch1:         0001-shell-Don-t-set-per-panel-icon.patch
Patch2:         0002-shell-Icon-name-helper-returns-symbolic-name.patch
Patch3:         0003-thunderbolt-new-panel-for-device-management.patch
Patch4:         0004-thunderbolt-move-to-the-Devices-page.patch

# Backport of F29 screen sharing UI
Patch5:         0001-sharing-Enable-settings-widget-for-gnome-remote-desk.patch

Patch6:         0001-wacom-Update-Test-your-settings-button-sensitivity-o.patch
Patch7:         0001-wacom-Update-to-newer-output-setting.patch

# Subscription management
Patch80001:     0001-info-Add-subscription-manager-integration.patch
Patch80002:     0002-info-Move-helper-for-getting-subscription-status-to-.patch
Patch80003:     0003-info-Update-registration-state-in-panel-when-it-happ.patch
Patch80004:     0004-info-Better-support-registered-but-no-subscriptions-.patch

Patch9:         0001-sharing-Fix-warning-when-disabling-sharing.patch
Patch10:        0001-network-Use-g_signal_connect_object-when-dealing-wit.patch

Patch11:        0001-common-fix-udev-based-device-removal.patch
Patch12:        0001-network-Keep-a-ref-on-NetDeviceEthernet-while-a-edit.patch
Patch13:        0001-network-Make-list-in-new-VPN-dialog-fill-up-space.patch
Patch14:        0001-network-Make-IPv4-v6-pages-drive-the-scrolledwindow-.patch
Patch15:        0001-network-Update-VPN-empty-label-status-after-removing.patch
Patch16:        0001-network-Use-connect-object-on-signals.patch
Patch17:        0001-sharing-Remember-the-password-on-remote-desktop-shar.patch
Patch18:        0001-wacom-Pick-libwacom-s-Generic-Pen-stylus-if-tool-ID-.patch

Patch20:        0001-user-Support-devices-with-more-than-5-enroll-steps.patch
Patch21:        backport-wacom-tool-id-fixes.patch
Patch22:        0001-power-correct-the-value-of-90-minutes-to-5400.patch
Patch23:        0001-sound-Ensure-to-preserve-sound-theme-when-changing-f.patch

Patch24:        categorize-infiniband.patch

Patch25:        printers-Update-entries.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1876291
Patch26:        Update-translations.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1938323
Patch31:        0001-network-Populate-AP-list-from-idle-handler.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1915411
Patch32:        0002-ce-page-security-add-SAE-support.patch
Patch33:        0003-ce-page-details-add-SAE-support.patch
Patch34:        0004-net-device-wifi-Decode-SAE-AP-security.patch
Patch35:        0005-network-complete-SAE-support.patch
Patch36:        0006-Add-support-for-Enhanced-Open-WiFi-security.patch
Patch37:        0007-network-Fix-connection-selection-and-SSID-display-fo.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1938944
Patch38:        0008-network-Fix-saving-passwords-for-non-wifi-connection.patch

# Backport monitor config policy (#2001655)
Patch39:        0001-display-Only-display-configuration-options-if-apply-.patch

Patch40:        0001-displays-Don-t-enlarge-display-panel-artificially.patch

# Workaround for libnma not handling OWE https://gitlab.gnome.org/GNOME/libnma/-/issues/9
Patch41:        0001-network-Fix-OWE-settings.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2097839
Patch42:        0001-timezone-use-blank-map.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2079139
Patch43:        0001-wifi-Move-airplane-mode-widget-above-the-main-stack.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1926995
Patch44:        0001-shell-Avoid-handling-map-events-from-other-windows.patch

BuildRequires:  chrpath
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl libxslt
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  libXxf86misc-devel
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
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gsettings_desktop_schemas_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libnm)
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
Requires: gnome-settings-daemon%{?_isa} >= 3.32.0-7
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: upower%{?_isa} >= %{upower_version}
%ifnarch s390 s390x
Requires: gnome-bluetooth%{?_isa} >= 1:%{gnome_bluetooth_version}
%endif

Requires: %{name}-filesystem = %{version}-%{release}
# For user accounts
Requires: accountsservice
Requires: alsa-lib
# For the thunderbolt panel
Requires: bolt
# For the color panel
Requires: colord
# For the printers panel
Requires: cups-pk-helper
Requires: dbus-x11
# For the info/details panel
Requires: glx-utils
# For the user languages
Requires: iso-codes
# For the network panel
Requires: nm-connection-editor
Recommends: NetworkManager-wifi
%if 0%{?fedora}
# For the sharing panel
Requires: rygel
%endif
# For the info/details panel
Requires: switcheroo-control
# For the keyboard panel
Requires: /usr/bin/gkbd-keyboard-display

Recommends: vino
Recommends: system-config-printer-libs

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
%autosetup -p1 -Sgit

%build
%meson -Ddocumentation=true
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
%doc AUTHORS NEWS README
%{_bindir}/gnome-control-center
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/gnome-control-center
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.SearchProvider.service
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.service
%{_datadir}/gettext/
%{_datadir}/glib-2.0/schemas/org.gnome.ControlCenter.gschema.xml
%{_datadir}/gnome-control-center/icons/
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_datadir}/gnome-control-center/pixmaps
%{_datadir}/gnome-control-center/sounds/gnome-sounds-default.xml
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

%files filesystem
%dir %{_datadir}/gnome-control-center
%dir %{_datadir}/gnome-control-center/keybindings
%dir %{_datadir}/gnome-control-center/sounds
%dir %{_datadir}/gnome/wm-properties

%changelog
* Mon Jan 02 2023 Felipe Borges <feborges@redhat.com> - 4.28.2-37
- Fix keyboard accessibility of screen resolution list
  Resolves: #1926995

* Mon Aug 15 2022 Felipe Borges <feborges@redhat.com> - 3.28.2-36
- Update airplane mode fix to synchronize with system changes
  Resolves: #2079139

* Fri Jul 15 2022 Felipe Borges <feborges@redhat.com> - 3.28.2-35
- Fix issue with the airplane mode toggle visibility on Wifi panel
  Resolves: #2079139

* Wed Jun 22 2022 Michael Catanzaro <mcatanzaro@redhat.com> - 3.28.2-34
- Remove timezone boundaries
  Resolves: #2097839

* Thu Feb 24 2022 Benjamin Berg <bberg@redhat.com> - 3.28.2-33
- Work around libnma not handling OWE
  Related: #2023156

* Thu Feb 10 2022 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-32
- Make displays panel able to fit in 800x600 resolution
  Resolves: #1893650

* Fri Feb 04 2022 Jonas Ådahl <jadahl@redhat.com> - 3.28.3-31
- Backport monitor config policy
  Resolves: #2001655

* Tue Jan 04 2022 Benjamin Berg <bberg@redhat.com> - 3.28.2-30
- Fix connection list AP selection and SSID display for OWE
  Resolves: #2023156
- Fix saving passwords for non-wifi connections
  Resolves: #1938944

* Wed Nov 10 2021 Benjamin Berg <bberg@redhat.com> - 3.28.2-29
- Backport SAE/WPA3/OWE support
  Resolves: #1915411
  Resolves: #2023156
- Add patch to fix wifi performance issue
  Resolves: #1938323

* Fri Sep 10 2021 Kalev Lember <klember@redhat.com> - 3.28.2-28
- Update pt_BR translations
- Resolves: #2003069

* Fri Jul 02 2021 Tomas Popela <tpopela@redhat.com> - 3.28.2-27
- Update fr, ja, zh_CN translations
- Resolves: #1933962

* Sun Jan 24 2021 Ray Strode <rstrode@redhat.com> - 3.28.2-26
- Support Simple Content Access from subscription manager
  Related: #1870837

* Thu Dec 03 2020 Marek Kasik <mkasik@redhat.com> - 3.28.2-25
- Fix a leak found by Coverity
- Related: #1700002

* Wed Dec 02 2020 Marek Kasik <mkasik@redhat.com> - 3.28.2-24
- Fix crashes when updating printer entries
- Related: #1700002
- Resolves: #1903043

* Tue Nov 24 2020 Marek Kasik <mkasik@redhat.com> - 3.28.2-23
- Update list of printers instead of regenerating it
- Resolves: #1700002

* Wed Sep 02 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-22
- Categorize Infiniband devices correctly
  Resolves: #1826379

* Mon Jun 29 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-21
- Honor sound theme changes when changing from the default theme
- Resolves: #1706008

* Mon Jun 29 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-20
- Fix 90min automatic sleep option to not last 80min
- Resolves: #1706076

* Fri Feb 21 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-19
- Backport tool serial/ID detection fixes
- Resolves: #1782517

* Thu Feb 13 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-18
- Pick "Generic Pen" correctly on unknown tool IDs
- Resolves: #1782517

* Thu Feb 13 2020 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-17
- Restore remote desktop password on wayland
- Resolves: #1763207

* Mon Jan 20 2020 Benjamin Berg <bberg@redhat.com> - 3.28.2-16
- Add patch to support more than 5 enroll steps
- Resolves: #1789474

* Mon Dec 16 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-15
- Fix another crash changing panel with Ethernet dialog opened
- Resolves: #1692299

* Fri Dec 13 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-14
- Restore placeholder label after removing last VPN connection
- Resolves: #1782425

* Fri Dec 13 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-13
- Make IPv4/v6 configuration pages scroll to focus
- Resolves: #1671709

* Fri Dec 13 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-12
- Fix spacing in "new VPN" dialog
- Resolves: #1656988

* Wed Dec 04 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-11
- Fix crash when changing panel with Ethernet dialog opened
- Resolves: #1692299

* Wed Dec 04 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-10
- Fix Wacom tablet removal on wayland session
- Resolves: #1658001

* Tue Dec 03 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-9
- Fix possible crash when closing the wifi panel
- Resolves: #1778668

* Mon Dec 01 2019 Tomas Pelka <tpelka@redhat.com> - 3.28.2-8
- Need rebuild in correct build target
- Resolves: #1749372

* Fri Nov 29 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-7
- Fix warning when disabling sharing
- Resolves: #1749372

* Mon Nov 18 2019 Kalev Lember <klember@redhat.com> - 3.28.2-6
- Add subscription manager integration
- Resolves: #1720251

* Tue Jul 23 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-5
- Update wacom panel to newer "output" setting
- Resolves: #1718133

* Mon Feb 11 2019 Carlos Garnacho <cgarnach@redhat.com> - 3.28.2-4
- Update "Test your settings" wacom button sensitivity on device availability
- Resolves: #1656995

* Thu Dec 13 2018 Marek Kasik <mkasik@redhat.com> - 3.28.2-3
- Recommend system-config-printer-libs as a dependency
- Resolves: #1637370

* Tue Aug 14 2018 Jonas Ådahl <jadahl@redhat.com> - 3.28.2-1
- Backport screen sharing UI (rhbz#1615810)

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
