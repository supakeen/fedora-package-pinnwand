Name:           pinnwand
Version:        1.3.2
Release:        1%{?dist}
Summary:        Straightforward pastebin software

License:        MIT
URL:            https://github.com/supakeen/pinnwand
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
pinnwand is Python pastebin software that tried to keep it simple but got a
little more complex
}

%description %_description

%prep
%autosetup -p1 -n pinnwand-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pinnwand

mkdir -p %{buildroot}/usr/share/pinnwand
cp -a pinnwand.service-example /%{buildroot}/usr/share/pinnwand/
cp -a pinnwand.toml-example /%{buildroot}/usr/share/pinnwand/

%check
%pytest

%files -f %{pyproject_files}
/usr/bin/pinnwand
/usr/share/pinnwand/pinnwand.service-example
/usr/share/pinnwand/pinnwand.toml-example

%doc README.rst
%license LICENSE

%changelog
* Sun Feb 20 2022 supakeen <cmdr@supakeen.com> - 1.3.2-1
- Initial version of the package.
