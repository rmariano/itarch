# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1402166967.031167
_enable_loop = True
_template_filename = u'/home/rmariano/.virtualenvs/lab/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/story.tmpl'
_template_uri = u'story.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'pheader', context._clean_inheritance_tokens(), templateuri=u'post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'pheader')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pheader = _mako_get_namespace(context, 'pheader')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 19
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 37
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer(u'\n<article class="storypage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    <header>\n        ')
        # SOURCE LINE 24
        __M_writer(unicode(pheader.html_title()))
        __M_writer(u'\n        ')
        # SOURCE LINE 25
        __M_writer(unicode(pheader.html_translations(post)))
        __M_writer(u'\n    </header>\n    <div itemprop="articleBody text">\n    ')
        # SOURCE LINE 28
        __M_writer(unicode(post.text()))
        __M_writer(u'\n    </div>\n')
        # SOURCE LINE 30
        if site_has_comments and enable_comments and not post.meta('nocomments'):
            # SOURCE LINE 31
            __M_writer(u'        <section class="comments">\n        <h2>')
            # SOURCE LINE 32
            __M_writer(unicode(messages("Comments")))
            __M_writer(u'</h2>\n        ')
            # SOURCE LINE 33
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer(u'\n        </section>\n')
        # SOURCE LINE 36
        __M_writer(u'</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        # SOURCE LINE 9
        if post.meta('keywords'):
            # SOURCE LINE 10
            __M_writer(u'        <meta name="keywords" content="')
            __M_writer(filters.html_escape(unicode(post.meta('keywords'))))
            __M_writer(u'">\n')
        # SOURCE LINE 12
        __M_writer(u'    <meta name="author" content="')
        __M_writer(unicode(post.author()))
        __M_writer(u'">\n    ')
        # SOURCE LINE 13
        __M_writer(unicode(helper.open_graph_metadata(post)))
        __M_writer(u'\n    ')
        # SOURCE LINE 14
        __M_writer(unicode(helper.twitter_card_information(post)))
        __M_writer(u'\n    ')
        # SOURCE LINE 15
        __M_writer(unicode(helper.meta_translations(post)))
        __M_writer(u'\n')
        # SOURCE LINE 16
        if post.description():
            # SOURCE LINE 17
            __M_writer(u'        <meta name="description" itemprop="description" content="')
            __M_writer(unicode(post.description()))
            __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


