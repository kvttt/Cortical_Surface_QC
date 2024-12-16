import pyvista as pv
import os
import matplotlib.pyplot as plt
import numpy as np


def extract_surfaces(file_path):
    # set file names
    lh_pial_fn = os.path.join(file_path, 'lh.pial.vtk')
    rh_pial_fn = os.path.join(file_path, 'rh.pial.vtk')
    lh_white_fn = os.path.join(file_path, 'lh.white.vtk')
    rh_white_fn = os.path.join(file_path, 'rh.white.vtk')

    # read surface files
    lh_pial = pv.read(lh_pial_fn)
    rh_pial = pv.read(rh_pial_fn)
    lh_white = pv.read(lh_white_fn)
    rh_white = pv.read(rh_white_fn)

    return lh_pial, rh_pial, lh_white, rh_white


def plot_lh_pial(lh_pial, file_path=None):
    # plot left hemisphere pial surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        lh_pial,
        scalars=lh_pial['thickness'],
        clim=[0, 5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    lhpr = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'lh_pial_r.png')
    # plotter.show(screenshot=save_fn)
    # plotter.close()

    # plot left hemisphere pial surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        lh_pial,
        scalars=lh_pial['thickness'],
        clim=[0, 5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    plotter.camera.azimuth = 180
    lhpl = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'lh_pial_l.png')
    # plotter.show(screenshot=save_fn)
    # plotter.close()

    return (
        lhpr, lhpl,
        np.percentile(lh_pial['thickness'], 5),
        np.percentile(lh_pial['thickness'], 95),
    )


def plot_rh_pial(rh_pial, file_path=None):
    # plot right hemisphere pial surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        rh_pial,
        scalars=rh_pial['thickness'],
        clim=[0, 5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    rhpr = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'rh_pial_r.png')
    # plotter.show(screenshot=save_fn)
    plotter.close()

    # plot right hemisphere pial surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        rh_pial,
        scalars=rh_pial['thickness'],
        clim=[0, 5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    plotter.camera.azimuth = 180
    rhpl = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'rh_pial_l.png')
    # plotter.show(screenshot=save_fn)
    plotter.close()

    return (
        rhpr, rhpl,
        np.percentile(rh_pial['thickness'], 5),
        np.percentile(rh_pial['thickness'], 95),
    )


def plot_lh_white(lh_white, file_path):
    # plot left hemisphere white surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        lh_white, 
        scalars=lh_white['curv'],
        clim=[-0.5, 0.5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    lhwr = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'lh_white_r.png')
    # plotter.show(screenshot=save_fn)
    plotter.close()

    # plot left hemisphere white surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        lh_white, 
        scalars=lh_white['curv'],
        clim=[-0.5, 0.5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    plotter.camera.azimuth = 180
    lhwl = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'lh_white_l.png')
    # plotter.show(screenshot=save_fn)
    plotter.close()

    # plot left hemisphere white surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        lh_white, 
        scalars=lh_white['curv'],
        clim=[-0.5, 0.5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    plotter.camera.azimuth = 225
    lhwlb = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'lh_white_lb.png')
    # plotter.show(screenshot=save_fn)
    plotter.close()

    # plot left hemisphere white surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        lh_white, 
        scalars=lh_white['curv'],
        clim=[-0.5, 0.5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    plotter.camera.azimuth = 135
    lhwlf = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'lh_white_lf.png')
    # plotter.show(screenshot=save_fn)
    plotter.close()

    return (
        lhwr, lhwl, lhwlb, lhwlf,
        np.percentile(lh_white['curv'], 5),
        np.percentile(lh_white['curv'], 95),
    )



def plot_rh_white(rh_white, file_path):
    # plot left hemisphere white surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        rh_white, 
        scalars=rh_white['curv'],
        clim=[-0.5, 0.5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    rhwr = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'rh_white_r.png')
    # plotter.show(screenshot=save_fn)
    plotter.close()

    # plot left hemisphere white surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        rh_white, 
        scalars=rh_white['curv'],
        clim=[-0.5, 0.5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    plotter.camera.azimuth = 180
    rhwl = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'rh_white_l.png')
    # plotter.show(screenshot=save_fn)
    plotter.close()

    # plot left hemisphere white surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        rh_white, 
        scalars=rh_white['curv'],
        clim=[-0.5, 0.5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    plotter.camera.azimuth = 45
    rhwrf = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'rh_white_rf.png')
    # plotter.show(screenshot=save_fn)
    plotter.close()

    # plot left hemisphere white surface
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(
        rh_white, 
        scalars=rh_white['curv'],
        clim=[-0.5, 0.5],
        cmap='jet',
        show_scalar_bar=False,
    )
    plotter.camera_position = 'yz'
    plotter.camera.zoom(1.6)
    plotter.camera.azimuth = -45
    rhwrb = plotter.screenshot(return_img=True)
    # plotter.show(auto_close=False)
    # save_fn = os.path.join(file_path, 'rh_white_rb.png')
    # plotter.show(screenshot=save_fn)
    plotter.close()

    return (
        rhwr, rhwl, rhwrf, rhwrb,
        np.percentile(rh_white['curv'], 5),
        np.percentile(rh_white['curv'], 95),
    )


def plot_all(file_path, output_path, index, group_num):
    lh_pial, rh_pial, lh_white, rh_white = extract_surfaces(file_path)
    lhpr, lhpl, lhp5, lhp95 = plot_lh_pial(lh_pial, file_path)
    rhpr, rhpl, rhp5, rhp95 = plot_rh_pial(rh_pial, file_path)
    lhwr, lhwl, lhwlb, lhwlf, lhw5, lhw95 = plot_lh_white(lh_white, file_path)
    rhwr, rhwl, rhwrf, rhwrb, rhw5, rhw95 = plot_rh_white(rh_white, file_path)

    ses_name = file_path.split('/')[-1]
    sub_name = file_path.split('/')[-2]

    output_fn = os.path.join(output_path, f'{index:02d}_{sub_name}_{ses_name}.pdf')

    fig = plt.figure(figsize=(16, 9), layout='constrained')
    subfigs = fig.subfigures(1, 2)

    ax = subfigs[0].subplots(3, 2)
    subfigs[0].suptitle(
        f'LH Thickness @ 5%: {lhp5:.2f}, 95%: {lhp95:.2f}\n'
        f'LH Curvature @ 5%: {lhw5:.2f}, 95%: {lhw95:.2f}',
        fontsize='x-large',
    )
    ax[0, 0].imshow(lhpl)
    ax[0, 0].axis('off')
    ax[0, 1].imshow(lhpr)
    ax[0, 1].axis('off')
    ax[1, 0].imshow(lhwl)
    ax[1, 0].axis('off')
    ax[1, 1].imshow(lhwr)
    ax[1, 1].axis('off')
    ax[2, 0].imshow(lhwlf)
    ax[2, 0].axis('off')
    ax[2, 1].imshow(lhwlb)
    ax[2, 1].axis('off')

    ax = subfigs[1].subplots(3, 2)
    subfigs[1].suptitle(
        f'RH Thickness @ 5%: {rhp5:.2f}, 95%: {rhp95:.2f}\n'
        f'RH Curvature @ 5%: {rhw5:.2f}, 95%: {rhw95:.2f}',
        fontsize='x-large',
    )
    ax[0, 0].imshow(rhpl)
    ax[0, 0].axis('off')
    ax[0, 1].imshow(rhpr)
    ax[0, 1].axis('off')
    ax[1, 0].imshow(rhwl)
    ax[1, 0].axis('off')
    ax[1, 1].imshow(rhwr)
    ax[1, 1].axis('off')
    ax[2, 0].imshow(rhwrf)
    ax[2, 0].axis('off')
    ax[2, 1].imshow(rhwrb)
    ax[2, 1].axis('off')

    fig.suptitle(
        f'Group {group_num:03d} #{index:02d} Subject {sub_name} Session {ses_name}', 
        fontsize='x-large',
    )
    fig.savefig(
        output_fn, 
        dpi=160, 
        metadata={
            'Author': 'Kaibo Tang', 
            'Creator': __file__
        },
    )
    plt.close(fig)

    return (
        f'{index:02d}_{sub_name}_{ses_name}.pdf',
        (lhp5 + rhp5) / 2,
        (lhp95 + rhp95) / 2,
        (lhw5 + rhw5) / 2,
        (lhw95 + rhw95) / 2,
    )
