update Programs 
    filter .id=<uuid>$program_id
    set {
        lesson -= (select detached Lessons 
            filter .id=<uuid>$lessons_id )
    }