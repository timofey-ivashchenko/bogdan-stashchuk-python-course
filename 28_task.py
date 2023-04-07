default_settings = {
    'editor.fontFamily': 'Courier New',
    'editor.insertSpaces': False,
    'editor.mouseWheelZoom': False,
    'editor.renderWhitespace': 'none',
    'editor.tabSize': 2,
    'editor.wordWrap': 'off',
    'files.trimTrailingWhitespace': False
}

team_settings = {
    'cSpell.language': 'en,ru',
    'editor.insertSpaces': True,
    'editor.rulers': [80],
    'editor.tabSize': 4,
    'editor.unicodeHighlight.allowedLocales': {
        'ru': True
    },
    'files.trimTrailingWhitespace': True,
    '[python]': {
        'editor.formatOnPaste': True,
        'editor.formatOnSave': True,
        'editor.formatOnType': True
    }
}

personal_settings = {
    'editor.fontFamily': 'JetBrains Mono',
    'editor.mouseWheelZoom': True,
    'editor.renderWhitespace': 'all',
    'editor.wordWrap': 'on',
    'explorer.confirmDelete': False,
    'git.openRepositoryInParentFolders': 'never',
    'python.defaultInterpreterPath': 'C:\\Program Files\\Python311\\python.exe',
    'security.workspace.trust.untrustedFiles': 'open',
    'workbench.colorTheme': 'One Dark Pro',
    'workbench.iconTheme': 'material-icon-theme'
}

result_settings = default_settings | team_settings | personal_settings

print(result_settings)
