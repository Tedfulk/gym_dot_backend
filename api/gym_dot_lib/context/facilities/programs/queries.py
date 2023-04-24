ADD_LESSON = r"""
select (
    update Programs
        filter .id=<uuid>$program_id
        set {
            lesson += (select detached Lessons
                filter .id=<uuid>$lesson_id )
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
"""

ALL_PROGRAMS = r"""
select Programs {
    id,
    name,
    description,
    active,
}
"""


CREATE_PROGRAM_WITH_LESSON = r"""
select (
insert Programs {
    name := <str>$name,
    description := <str>$description,
    active := <bool>$active,
    lesson := {
    (insert Lessons {
        class_dates := <array<cal::local_date>>$class_dates,
        class_times := <array<cal::local_time>>$class_times,
        len_of_class_time := <int32>$len_of_class_time,
        active := <bool>$active,
        max_attendees := <int32>$max_attendees,
        min_attendees := <int32>$min_attendees,
        waitlist := <int32>$waitlist,
    }
    )
    }
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
"""

CREATE_PROGRAM = r"""
select (
    insert Programs {
        name := <str>$name,
        description := <str>$description,
        active := <bool>$active,
    }
) {
    id,
    name,
    description,
    active,
}
"""


DELETE_PROGRAM = r"""
delete Programs
    filter .id = <uuid>$program_id
"""

GET_LESSONS = r"""
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
"""

GET_PROGRAM = r"""
select Programs {
    id,
    name,
    description,
    active,
} filter .id = <uuid>$program_id
"""


REMOVE_LESSON = r"""
select (
    update Programs
        filter .id=<uuid>$program_id
        set {
            lesson -= (select detached Lessons
                filter .id=<uuid>$lesson_id )
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
"""


UPDATE_PROGRAM = r"""
select (
    update Programs
    filter .id = <uuid>$program_id
    set {
        name := <str>$name,
        description := <str>$description,
        active := <bool>$active,
    }
) {
    id,
    name,
    description,
    active,
}
"""
