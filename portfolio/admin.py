from django.contrib import admin
from .models import (
    Profile,
    Skill,
    Education,
    Experience,
    Internship,
    Service,
    Project,
    Certificate,
    Contact
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "designation",
        "email",
        "phone",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "skill_name",
        "percentage",
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "degree",
        "institution",
        "year",
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "role",
        "duration",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "technologies",
        "featured",
    )

    list_filter = (
        "featured",
    )

    search_fields = (
        "title",
        "technologies",
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "organization",
        "year",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )

    readonly_fields = (
        "created_at",
    )

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "role",
        "duration",
    )

    