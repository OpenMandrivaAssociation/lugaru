%global _prefix %{_prefix}/games/%{name}

Name: lugaru
Version: 1.2
Release: 1
URL: https://osslugaru.gitlab.io
Source0: https://bitbucket.org/osslugaru/lugaru/downloads/lugaru-%{version}.tar.xz
Group: Games/Action
Summary: Third-person action game
License: Creative Commons Attribution-ShareAlike 4.0
BuildRequires: cmake ninja
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(vorbisfile)

%description
Lugaru (pronounced Loo-GAH-roo) is a third-person action game. The main
character, Turner, is an anthropomorphic rebel bunny rabbit with impressive
combat skills.

In his quest to find those responsible for slaughtering his village, he
uncovers a far-reaching conspiracy involving the corrupt leaders of the
rabbit republic and the starving wolves from a nearby den.

Turner takes it upon himself to fight against their plot and save his
fellow rabbits from slavery.

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
mkdir -p \
	%{buildroot}%{_bindir} \
	%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/pixmaps
cat >%{buildroot}%{_bindir}/%{name} <<'EOF'
#!/bin/sh
cd %{_prefix}
exec ./%{name}
EOF
chmod +x %{buildroot}%{_bindir}/%{name}
cat >%{buildroot}%{_datadir}/applications/%{name}.desktop <<'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Lugaru
GenericName=Action Game
Comment=Action Game
Icon=%{name}
Exec=%{_bindir}/%{name}
Categories=Game;ActionGame;
EOF
cp Dist/Linux/lugaru.png %{buildroot}%{_datadir}/pixmaps/

%files
%{_prefix}
%{_bindir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
