from html import escape

from streamlit.runtime.uploaded_file_manager import UploadedFile


def dict_to_email_html(
    data: dict,
    title: str = "Details",
) -> str:
    """
    Convert a nested dict into clean, email-safe HTML.
    """

    def render_value(value, level=0):
        if isinstance(value, dict):
            return render_dict(value, level + 1)

        if isinstance(value, list):
            items = "".join(
                f"<li style='margin-bottom:6px;'>{render_value(v, level + 1)}</li>"
                for v in value
            )
            return f"""
                <ul style="
                    margin: 6px 0 12px 18px;
                    padding: 0;
                    color: #333;
                    font-size: 14px;
                ">
                    {items}
                </ul>
            """

        if isinstance(value, UploadedFile):
            value = value.name

        return escape(str(value))

    def render_dict(d: dict, level=0):
        rows = []

        for key, value in d.items():
            key_html = escape(str(key).replace("_", " ").title())

            if isinstance(value, dict):
                rows.append(f"""
                    <tr>
                        <td colspan="2" style="
                            padding: 12px 8px 6px;
                            font-weight: 600;
                            font-size: 15px;
                            color: #1f2937;
                            border-top: 1px solid #e5e7eb;
                        ">
                            {key_html}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2" style="padding-left: 12px;">
                            {render_dict(value, level + 1)}
                        </td>
                    </tr>
                """)
            else:
                rows.append(f"""
                    <tr>
                        <td style="
                            padding: 6px 8px;
                            width: 35%;
                            color: #6b7280;
                            font-size: 13px;
                            vertical-align: top;
                        ">
                            {key_html}
                        </td>
                        <td style="
                            padding: 6px 8px;
                            color: #111827;
                            font-size: 14px;
                        ">
                            {render_value(value, level + 1)}
                        </td>
                    </tr>
                """)

        return f"""
            <table width="100%" cellpadding="0" cellspacing="0" style="
                border-collapse: collapse;
                margin-bottom: 12px;
            ">
                {''.join(rows)}
            </table>
        """

    html = f"""
    <div style="
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
        background-color: #ffffff;
        color: #111827;
        line-height: 1.5;
    ">
        <h2 style="
            font-size: 18px;
            margin-bottom: 12px;
            color: #111827;
        ">
            {escape(title)}
        </h2>

        <div style="
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 12px 16px;
            background-color: #fafafa;
        ">
            {render_dict(data)}
        </div>
    </div>
    """

    return html.strip()