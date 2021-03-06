from ckan.plugins import toolkit
from ckanext.issues import model as issuemodel


is_positive_integer = toolkit.get_validator('is_positive_integer')


def is_valid_status(value, context):
    if value in issuemodel.ISSUE_STATUS:
        return value
    else:
        raise toolkit.Invalid(toolkit._(
            '{0} is not a valid status'.format(value))
        )


def is_valid_sort(filter_string, context):
    try:
        return issuemodel.IssueFilter[filter_string]
    except KeyError:
        msg_str = 'Cannot apply filter. "{0}" is not a valid filter'
        raise toolkit.Invalid(
            toolkit._(msg_str.format(filter_string))
        )


def as_package_id(package_id_or_name, context):
    '''given a package_id_or_name, return just the package id'''
    model = context['model']
    package = model.Package.get(package_id_or_name)
    if not package:
        raise toolkit.Invalid('%s: %s' % (toolkit._('Not found'),
                                          toolkit._('Dataset')))
    else:
        return package.id


def issue_exists(issue_id, context):
    issue_id = is_positive_integer(issue_id, context)
    result = issuemodel.Issue.get(issue_id, session=context['session'])
    if not result:
        raise toolkit.Invalid(toolkit._('Issue not found') + ': %s' % issue_id)
    return issue_id

def issue_comment_exists(issue_comment_id, context):
    issue_comment_id = is_positive_integer(issue_comment_id, context)
    result = issuemodel.IssueComment.get(issue_comment_id, session=context['session'])
    if not result:
        raise toolkit.Invalid(toolkit._('Issue Comment not found') + ': %s' % issue_comment_id)
    return issue_comment_id
