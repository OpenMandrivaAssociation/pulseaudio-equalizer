# This file based on Fedora specfile for package pulseaudio-equalizer

Name:           pulseaudio-equalizer
Version:        0.1
Release:        0.20100205.1
Summary:        A 15 Bands Equalizer for PulseAudio

Group:          Sound
License:        GPLv3+
URL:            https://code.launchpad.net/~psyke83/+junk/%{name}
# This is a bzr checkout, to obtain the used tarball in this spec :
# bzr branch lp:~psyke83/+junk/pulseaudio-equalizer
# mv %%{name} %%{name}-%%{version}
# tar cJf %%{name}-%%{version}.tar.xz %%{name}-%%{version} --exclude .bzr
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.1
Source2:        %{name}-gtk.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  desktop-file-utils

Requires:       pygtk2 >= 2.4
Requires:       swh-plugins gnome-icon-theme
Requires:       pulseaudio-utils >= 0.9.19

# Force default equalizer persistence value, fixes rhbz #635400
Patch0:         pulseaudio-equalizer-0.1-fedora-force-default-persistence-value.patch
# Remove preamp per discussion with upstrem, fixes rhbz #639604
Patch1:         pulseaudio-equalizer-0.1-fedora-remove-preamp.patch
# Better search for the window icon, fixes rhbz #632940
Patch2:         pulseaudio-equalizer-0.1-fedora-window-icon.patch
# Do not crash on missing preset, fixes rhbz ##679005
Patch3:         pulseaudio-equalizer-0.1-fedora-do-not-crash-on-missing-preset.patch

%description
PulseAudio Equalizer is a 15 bands system wide equalizer, that means
any application that is using PulseAudio, will benefit from the sound
improvement.

%prep
%setup -q
cp debian/copyright COPYING
cp debian/changelog ChangeLog
sed -i 's|gnome-volume-control|multimedia-volume-control|g' usr/share/applications/pulseaudio-equalizer.desktop
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build


%install
mkdir -p %{buildroot}
cp -rp usr %{buildroot}
install -Dpm 644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/%{name}.1
install -Dpm 644 %{SOURCE2} %{buildroot}/%{_mandir}/man1/%{name}-gtk.1

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}-gtk
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-gtk.1.*
