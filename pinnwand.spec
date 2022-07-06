Name:           pinnwand
Version:        1.3.1
Release:        1%{?dist}
Summary:        A Token Bucket implementation.

License:        MIT
URL:            https://github.com/supakeen/pinnwand
Source0:        %{pypi_source pinnwand}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
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

%check
%pytest

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Sun Feb 20 2022 supakeen <cmdr@supakeen.com>
- Initial version of the package.
