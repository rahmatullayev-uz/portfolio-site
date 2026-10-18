from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    # Spam botlarni ushlash uchun yashirin maydon (Honeypot)
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput(attrs={"tabindex": "-1", "autocomplete": "off"}),
        label="",
    )

    class Meta:
        model = ContactMessage
        fields = ["sender_name", "sender_email", "subject", "message"]
        widgets = {
            "sender_name": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-3 rounded-xl bg-zinc-50 dark:bg-zinc-900/60 border border-zinc-200 dark:border-zinc-800 text-sm text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/30 focus:border-emerald-500 transition-all",
                    "placeholder": "Ismingiz yoki kompaniya",
                    "required": True,
                }
            ),
            "sender_email": forms.EmailInput(
                attrs={
                    "class": "w-full px-4 py-3 rounded-xl bg-zinc-50 dark:bg-zinc-900/60 border border-zinc-200 dark:border-zinc-800 text-sm text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/30 focus:border-emerald-500 transition-all",
                    "placeholder": "sizning.emailingiz@example.com",
                    "required": True,
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-3 rounded-xl bg-zinc-50 dark:bg-zinc-900/60 border border-zinc-200 dark:border-zinc-800 text-sm text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/30 focus:border-emerald-500 transition-all",
                    "placeholder": "Xabar mavzusi (ixtiyoriy)",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "w-full px-4 py-3 rounded-xl bg-zinc-50 dark:bg-zinc-900/60 border border-zinc-200 dark:border-zinc-800 text-sm text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/30 focus:border-emerald-500 transition-all",
                    "placeholder": "Taklifingiz, loyiha tavsifi yoki savolingizni yozing...",
                    "rows": 5,
                    "required": True,
                }
            ),
        }

    def clean_honeypot(self):
        honeypot_val = self.cleaned_data.get("honeypot")
        if honeypot_val:
            raise forms.ValidationError("Spam aniqlandi.")
        return honeypot_val
