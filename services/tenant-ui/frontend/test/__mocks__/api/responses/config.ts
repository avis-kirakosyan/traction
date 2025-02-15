const config = {
  frontend: {
    tenantProxyPath: 'http://localhost:8032',
    apiPath: 'api/',
    basePath: '/',
    showDeveloper: true,
    showInnkeeperReservationPassword: true,
    showInnkeeperAdminLogin: true,
    oidc: {
      active: false,
      authority:
        'https://dev.loginproxy.gov.bc.ca/auth/realms/digitaltrust-nrm',
      client: 'innkeeper-frontend',
      label: 'IDIR',
    },
    ux: {
      appTitle: 'Traction Tenant Console',
      appInnkeeperTitle: 'Traction Innkeeper Console',
      sidebarTitle: 'TRACTION',
      copyright: '',
      owner: '',
      coverImageCopyright: 'Photo by Kristoffer Fredriksson on StockSnap',
      aboutBusiness: {
        title: 'Government of British Columbia',
        linkTitle: 'BC Digital Trust Service Agreement',
        link: 'https://github.com/bcgov/bc-vcpedia/blob/main/agents/bc-gov-agent-service.md',
        imageUrl: '/img/bc/bc_logo.png',
      },
    },
    ariesDetails: {
      acapyVersion: '0.8.1',
      ledgerName: 'bcovrin-test',
      ledgerBrowser: 'http://test.bcovrin.vonx.io',
      tailsServer: 'https://tails-test.vonx.io',
    },
  },
  image: {
    buildtime: '',
    tag: 'tenant-ui:default',
    version: 'default',
  },
  server: {
    tractionUrl: 'http://localhost:5100',
  },
};

const plugins = {
  result: [
    'aries_cloudagent.holder',
    'aries_cloudagent.ledger',
    'aries_cloudagent.messaging.credential_definitions',
  ],
};

function setTenantProxyUrl(url: string) {
  config.frontend.tenantProxyPath = url;
}

export default {
  config,
  plugins,
  setTenantProxyUrl,
};
