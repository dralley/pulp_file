# coding=utf-8
"""Utilities for tests for the file plugin."""
from functools import partial
from unittest import SkipTest

from pulp_smash import api, selectors, utils
from pulp_smash.pulp3.constants import REPO_PATH
from pulp_smash.pulp3.utils import (
    gen_publisher,
    gen_remote,
    gen_repo,
    get_added_content,
    get_content,
    get_removed_content,
    require_pulp_3,
    require_pulp_plugins,
    sync,
)

from pulp_file.tests.functional.constants import (
    FILE_CONTENT_NAME,
    FILE_CONTENT_PATH,
    FILE_FIXTURE_MANIFEST_URL,
    FILE_REMOTE_PATH
)


def populate_pulp(cfg, url=None):
    """Add file contents to Pulp.

    :param pulp_smash.config.PulpSmashConfig: Information about a Pulp
        application.
    :param url: The URL to a file repository's ``PULP_MANIFEST`` file. Defaults
        to :data:`pulp_smash.constants.FILE_FIXTURE_URL` + ``PULP_MANIFEST``.
    :returns: A list of dicts, where each dict describes one file content in
        Pulp.
    """
    if url is None:
        url = FILE_FIXTURE_MANIFEST_URL

    client = api.Client(cfg, api.json_handler)
    remote = {}
    repo = {}
    try:
        remote.update(client.post(FILE_REMOTE_PATH, gen_remote(url)))
        repo.update(client.post(REPO_PATH, gen_repo()))
        sync(cfg, remote, repo)
    finally:
        if remote:
            client.delete(remote['_href'])
        if repo:
            client.delete(repo['_href'])
    return client.get(FILE_CONTENT_PATH)['results']


def gen_file_remote(url=None, **kwargs):
    """Return a semi-random dict for use in creating a file Remote.

    :param url: The URL of an external content source.
    """
    if url is None:
        url = FILE_FIXTURE_MANIFEST_URL

    return gen_remote(url, **kwargs)


def gen_file_publisher(**kwargs):
    """Return a semi-random dict for use in creating a file Remote.

    :param url: The URL of an external content source.
    """
    return gen_publisher(**kwargs)


def gen_file_content_attrs(artifact):
    """Generate a dict with content unit attributes.

    :param artifact: A dict of info about the artifact.
    :returns: A semi-random dict for use in creating a content unit.
    """
    return {'artifact': artifact['_href'], 'relative_path': utils.uuid4()}


def get_file_content(repo, version_href=None):
    """Return the content units present in a file repository.

    :param repo: A dict of information about the repository.
    :param version_href: Optional repository version.
    :returns: A list of filecontent units present in a given repository.
    """
    return get_content(repo, version_href)[FILE_CONTENT_NAME]


def get_file_added_content(repo, version_href=None):
    """Return the content units added in a file repository version.

    :param repo: A dict of information about the repository.
    :param version_href: Optional repository version.
    :returns: A list of filecontent units present in a given repository.
    """
    return get_added_content(repo, version_href)[FILE_CONTENT_NAME]


def get_file_removed_content(repo, version_href=None):
    """Return the content units removed in a file repository version.

    :param repo: A dict of information about the repository.
    :param version_href: Optional repository version.
    :returns: A list of filecontent units present in a given repository.
    """
    return get_removed_content(repo, version_href)[FILE_CONTENT_NAME]


def get_file_content_paths(repo):
    """Return the relative path of content units present in a file repository.

    :param repo: A dict of information about the repository.
    :returns: A list with the paths of units present in a given repository.
    """
    # The "relative_path" is actually a file path and name
    return [content_unit['relative_path'] for content_unit in get_file_content(repo)]


def set_up_module():
    """Skip tests Pulp 3 isn't under test or if pulp-file isn't installed."""
    require_pulp_3(SkipTest)
    require_pulp_plugins({'pulp_file'}, SkipTest)


skip_if = partial(selectors.skip_if, exc=SkipTest)  # pylint:disable=invalid-name
"""The ``@skip_if`` decorator, customized for unittest.

:func:`pulp_smash.selectors.skip_if` is test runner agnostic. This function is
identical, except that ``exc`` has been set to ``unittest.SkipTest``.
"""
