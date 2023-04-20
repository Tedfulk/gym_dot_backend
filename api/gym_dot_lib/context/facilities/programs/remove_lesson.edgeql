select (
    update Programs
        filter .id=<uuid>$program_id
        set {
            lesson -= (select detached Lessons
                filter .id=<uuid>$lessons_id )
        }
        ) {
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
