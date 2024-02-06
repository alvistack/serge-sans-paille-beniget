# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-beniget
Epoch: 100
Version: 0.4.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Extract semantic information about static Python code
License: BSD-3-Clause
URL: https://github.com/serge-sans-paille/beniget/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A static analyzer for Python2 and Python3 code.Beniget provides a static
over-approximation of the global and local definitions inside Python
Module/Class/Function. It can also compute def-use chains from each
definition.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-beniget
Summary: Extract semantic information about static Python code
Requires: python3
Requires: python3-gast >= 0.5.0
Provides: python3-beniget = %{epoch}:%{version}-%{release}
Provides: python3dist(beniget) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-beniget = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(beniget) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-beniget = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(beniget) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-beniget
A static analyzer for Python2 and Python3 code.Beniget provides a static
over-approximation of the global and local definitions inside Python
Module/Class/Function. It can also compute def-use chains from each
definition.

%files -n python%{python3_version_nodots}-beniget
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-beniget
Summary: Extract semantic information about static Python code
Requires: python3
Requires: python3-gast >= 0.5.0
Provides: python3-beniget = %{epoch}:%{version}-%{release}
Provides: python3dist(beniget) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-beniget = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(beniget) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-beniget = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(beniget) = %{epoch}:%{version}-%{release}

%description -n python3-beniget
A static analyzer for Python2 and Python3 code.Beniget provides a static
over-approximation of the global and local definitions inside Python
Module/Class/Function. It can also compute def-use chains from each
definition.

%files -n python3-beniget
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-beniget
Summary: Extract semantic information about static Python code
Requires: python3
Requires: python3-gast >= 0.5.0
Provides: python3-beniget = %{epoch}:%{version}-%{release}
Provides: python3dist(beniget) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-beniget = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(beniget) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-beniget = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(beniget) = %{epoch}:%{version}-%{release}

%description -n python3-beniget
A static analyzer for Python2 and Python3 code.Beniget provides a static
over-approximation of the global and local definitions inside Python
Module/Class/Function. It can also compute def-use chains from each
definition.

%files -n python3-beniget
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
