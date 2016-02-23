#ifndef TRANSPARENT_H_
#define TRANSPARENT_H_

#include <iostream>
#include <gtk/gtk.h>
#include <gtkmm/window.h>
#include <gtkmm/button.h>
#include <gtkmm/alignment.h>

class Transparent : public Gtk::Window
{

private:
    std::string _buttonLabel;

public:
    Transparent();
    void set_visual(Glib::RefPtr<Gdk::Visual> visual);
    virtual ~Transparent();

protected:
    // Signal handlers:
    // Note that on_draw is actually overriding a virtual function
    // from the Gtk::Window class. I set it as virtual here in case
    // someone wants to override it again in a derived class.
    void on_button_clicked();
    virtual bool on_draw(const ::Cairo::RefPtr< ::Cairo::Context>& cr);
    void on_screen_changed(const Glib::RefPtr<Gdk::Screen>& previous_screen);
    bool on_window_clicked(GdkEventButton* event);

    // Member widgets:
    Gtk::Alignment _alignment;
    Gtk::Button _button;

    bool _SUPPORTS_ALPHA = false;

};

#endif /* TRANSPARENT_H_ */