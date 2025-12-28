import streamlit as st
from typing import List, Optional


class FileType:
    IMAGE = "image"
    PDF = "pdf"
    DOC = "doc"

    _EXTENSIONS = {
        IMAGE: ["png", "jpg", "jpeg"],
        PDF: ["pdf"],
        DOC: ["doc", "docx"],
    }

    @classmethod
    def extensions(cls, types: List[str]) -> list[str]:
        exts = []
        for t in types:
            exts.extend(cls._EXTENSIONS.get(t, []))
        return exts


class FileInput:
    """
    Streamlit file input component.
    Supports image, pdf, and doc/docx uploads.
    """

    def __init__(
            self,
            name: str,
            label: str,
            context_help_string: str,
            key_prefix: str,
            allowed_types: List[str],
            required: bool = False,
            help_text: Optional[str] = None,
            multiple: bool = False,
    ):
        self.name = name
        self.label = label
        self.context_help_string = context_help_string
        self.key_prefix = key_prefix
        self.allowed_types = allowed_types
        self.required = required
        self.help_text = help_text
        self.multiple = multiple

    def render(self):
        st.caption(self.context_help_string)
        context = st.text_input("Context", value="" or "", key=f"{self.key_prefix}_context")

        key = f"{self.key_prefix}_{self.name}"
        files = st.file_uploader(
            self.label,
            type=FileType.extensions(self.allowed_types),
            accept_multiple_files=self.multiple,
            key=key,
        )

        if self.help_text:
            st.caption(self.help_text)

        if self.required and not files:
            st.error("This file is required.")

        return context, files
