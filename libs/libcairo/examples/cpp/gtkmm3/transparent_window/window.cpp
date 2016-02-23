#include "window.h"

Transparent::Transparent() :
    _buttonLabel("Button1"),
    _alignment(Gtk::ALIGN_START, Gtk::ALIGN_START, 0.0, 0.0),    // Aligns the button.
    _button(_buttonLabel)                                        // Creates a new button with label '_buttonLabel'.
{

    // Set up the top-level window.
    set_title("Transparency test");
    set_default_size(400,400);
    set_decorated(false);
    add_events(Gdk::BUTTON_PRESS_MASK);
    set_position(Gtk::WIN_POS_CENTER);
    set_app_paintable(true);

    // Signal handlers
    signal_draw().connect(sigc::mem_fun(*this, &Transparent::on_draw));
    signal_screen_changed().connect(sigc::mem_fun(*this, &Transparent::on_screen_changed));
    signal_button_press_event().connect(sigc::mem_fun(*this, &Transparent::on_window_clicked));
    _button.signal_clicked().connect(sigc::mem_fun(*this, &Transparent::on_button_clicked));

    // Widgets

    on_screen_changed(get_screen());

    // This will add the aligner.
    add(_alignment);

    // Now pack the button into the aligner.
    _alignment.add(_button);

    // Set up the button
    _button.set_size_request(100, 100);

    // Show the window and all its children.
    show_all();
}

Transparent::~Transparent()
{
}

void Transparent::on_button_clicked()
{
    std::cout << "The button '" << _buttonLabel << "' was pressed." << std::endl;
}

bool Transparent::on_draw(const Cairo::RefPtr<Cairo::Context>& cr)
{
    cr->save();
    if (_SUPPORTS_ALPHA) {
        cr->set_source_rgba(0.5, 1.0, 0.5, 0.5);    // transparent
    } else {
        cr->set_source_rgb(0.5, 1.0, 0.5);          // opaque
    }
    cr->set_operator(Cairo::OPERATOR_SOURCE);
    cr->paint();
    cr->restore();

    return Gtk::Window::on_draw(cr);
}

/**
 * Checks to see if the display supports alpha channels
 */
void Transparent::on_screen_changed(const Glib::RefPtr<Gdk::Screen>& previous_screen) {
    auto screen = get_screen();
    auto visual = screen->get_rgba_visual();

    if (!visual) {
        std::cout << "Your screen does not support alpha channels!" << std::endl;
    } else {
        std::cout << "Your screen supports alpha channels!" << std::endl;
        _SUPPORTS_ALPHA = TRUE;
    }

    set_visual(visual);
}

/**
 * This simply adds a method which seems to be missing in Gtk::Widget,
 * so I had to use Gtk+ manually.
 *
 * Sets the visual for 'this' (the current widget).
 */
void Transparent::set_visual(Glib::RefPtr<Gdk::Visual> visual) {
    gtk_widget_set_visual(GTK_WIDGET(gobj()), visual->gobj());
}

/**
 * If I click somewhere other than the button, this toggles
 * between having window decorations and not having them.
 */
bool Transparent::on_window_clicked(GdkEventButton* event) {
    set_decorated(!get_decorated());
    return false;
}