[next]: img/next.png "Mkdocs website next navigation title"
[title]: img/title.png "Mkdocs website title"
[web_nav]: img/website_navigation.png "Mkdocs website navigation tree structure"

# mkdocs-tree-title

This is a MkDocs plugin that adds a tree title for each page. It is composed from the ancestors tree titles and the page title and it is set on the page as tree_title attribute.

This can be usefull for the meta title as well as the next and previus titles in the material mkdocs theme.

## Setup

Install the plugin using pip:

`pip install mkdocs-tree-title`

Activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - search
  - tree-title
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

More information about plugins in the [MkDocs documentation][mkdocs-plugins].

## Config

* `join_string` - The joining string of the tree titles

  By default the joining string is a space, if you want to change it to a different one you can do so by adding the argument:
  ```yaml
  plugins:
    - search
    - tree-title:
      join_string: " - "
  ```

## Usage

Having a mkdocs nav configuration as follows:
```yml
nav:
    - Ebike Settings:
        - Overview: ebike_settings/overview.md
        - Bafang:
            - Overview: ebike_settings/bafang/overview.md
            - Basic: ebike_settings/bafang/basic.md
            - Pedal: ebike_settings/bafang/pedal.md
            - Throttle: ebike_settings/bafang/throttle.md
            - Torque: ebike_settings/bafang/torque.md
        - Lishui: ebike_settings/lishui.md
```

![Mkdocs website navigation tree structure][title]

### Template Title

```html
{% block htmltitle %}
    <title>{% if page and page.title and not page.is_homepage %}{{ page.tree_title }} | {% endif %}{{ config.site_name }}</title>
{% endblock %}
```

![Mkdocs website title][title]

### Template Navigation

```html
{% if page.next_page %}
  <a href="{{ page.next_page.url | url }}" title="{{ page.next_page.title | striptags }}" class="md-footer-nav__link md-footer-nav__link--next" rel="next">
    <div class="md-footer-nav__title">
      <div class="md-ellipsis">
        <span class="md-footer-nav__direction">
          {{ lang.t("footer.next") }}
        </span>
        {{ page.next_page.tree_title }}
      </div>
    </div>
    <div class="md-footer-nav__button md-icon">
    </div>
  </a>
{% endif %}
```

![Mkdocs website next navigation title][next]

## See Also

More information about templates [here][mkdocs-template].

More information about blocks [here][mkdocs-block].

[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/
[mkdocs-template]: https://www.mkdocs.org/user-guide/custom-themes/#template-variables
[mkdocs-block]: https://www.mkdocs.org/user-guide/styling-your-docs/#overriding-template-blocks
