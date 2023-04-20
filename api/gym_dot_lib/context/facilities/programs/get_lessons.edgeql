select Programs {
    id,
    name,
    description,
    active,
    lesson: {
        id,
        class_dates,
        class_times,
        len_of_class_time,
        active,
        max_attendees,
        min_attendees,
        waitlist,
    }
}
filter .id=<uuid>$program_id
